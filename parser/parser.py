
import sys
import re
import os
import csv
import pymupdf
import PIL.Image
import io   
import shutil
    
sys.stdout.reconfigure(encoding='utf-8')

def clean_dir():
    for a in ['_idx_imgs','_imgs']:
        if os.path.isdir(a):
            shutil.rmtree(a)
        os.makedirs(a, exist_ok=True)


class QPdfLine():
    def __init__(self, text, font):
        self.text = text
        self.font = font

class QPdfSlikeName():
    def __init__(self, text, line):
        self.text = text
        self.line = line
        
class QParser():
    def __init__(self, filename_, category, pattern_q_, pattern_a_, pattern_b_, pattern_c_, pattern_d_, num_question  ):
        self.category = category
        self.num_question = num_question
        self.filename = filename_
        self.q_number = 1
        self._round = 10
        self.pattern_tab = r"\t"
        self.pattern_slike = r"Slika"
        self.pattern_skip = [r'Period važenja', r'(\d+) \/ (\d+)', r'^Slika br']
        self.pattern_answer = 'Pregled tačnih odgovora'
        self.answer = {}
        self.pattern_q_ = pattern_q_
        self.pattern_q = pattern_q_.replace('{number}',str(self.q_number))
        self.pattern_a = pattern_a_
        self.pattern_b = pattern_b_
        self.pattern_c = pattern_c_
        self.pattern_d = pattern_d_

        self.str_q = ""
        self.str_a = ""
        self.str_b = ""
        self.str_c = ""
        self.str_d = ""
        self.in_str = ""
        self.lines=[]
        self.slike={}
        self.question_to_images={}
        self.fieldnames = ['number','question', 'a','b','c','d','right_answer','category','img']

       
    def parse_lines(self, round = 10, parse_slike = True, images_idx = True):
        self._round = int(round)
        self.parse_words()
        if parse_slike:
            self.parse_slike()
        if images_idx:
            self.parse_images_just()
        #self.parse_block()
        #self.parse_dict()
                       
        i = 0
        self.l_line = len(self.lines) - 1                    
        while i < self.l_line:        
            i = i + 1
            l = self.lines[i]
            match_obj = re.match(self.pattern_answer, l)
            if match_obj:
                break
        while i < self.l_line:
            i = i + 1
            l = self.lines[i]
            match = re.findall(r"(\d+)\. - (\d)", l)
            for e in match:
                if len(e) == 2:
                    self.answer[int(e[0])]=self.format_answer(int(e[1])) 

    def parse_slike(self):
        doc = pymupdf.open(f"pdf/{self.filename}") # open a document
        imgDir = "_imgs"
        os.makedirs(imgDir, exist_ok=True)
        strpage=0
        for page in doc:
            # Extract words with coordinates
            words = page.get_text("words", sort=True)
            # Extract images with bounding boxes
            images = page.get_images(full=True)
            img_info_list = [(img[0], page.get_image_bbox(img)) for img in images]

            for idx, (xref, bbox) in enumerate(img_info_list):
                img_x0, img_y0, img_x1, img_y1 = bbox

                if img_y0 < 10:
                    continue
                # Collect words *under the image*
                caption_words = []
                for w in words:
                    #print (w)
                    x0 = w[0]
                    x1 = w[2]
                    y0 = w[1]
                    y1 = w[3]
                    t = w[4]
                    #if t == 'Slika':
                        #print (f"{img_x0} {x0} {x1} {img_x1} {t} ")
                        #print (f" {y0} > {img_y1}  {t} ")
                    if img_x0  <= x0 and x0 <= img_x1 and y0 > img_y1 and y1 < img_y1+50  :
                        #print ('appned')
                        caption_words.append(w[4])
              
                if caption_words:
                    caption_text = " ".join(caption_words).strip()
                    match_obj = re.match(self.pattern_slike, caption_text)
                    if match_obj:
                        t = self.make_image_hash(caption_text)
                        self.slike[t]=f'{imgDir}/{self.category}-{caption_text}.png' 
                else:
                    caption_text = f"page{strpage}_img{idx}"
                    

                data = doc.extract_image(xref)
                with PIL.Image.open(io.BytesIO(data.get('image'))) as image:
                    image.save(f'{imgDir}/{self.category}-{caption_text}.png', mode='wb')
            strpage=strpage+1
        doc.close()
         

    def parse_images_just(self):
        doc = pymupdf.open(f"pdf/{self.filename}") # open a document
        strpage=0
        imgDir = "_idx_imgs"
        os.makedirs(imgDir, exist_ok=True)
        for page in doc: # iterate the document pages
            imageList = doc.get_page_images(strpage, full=False)

            idx = 0
            if imageList:
                
                for img in reversed(imageList):
                    data = doc.extract_image(img[0])
                    with PIL.Image.open(io.BytesIO(data.get('image'))) as image:
                        name = f'{imgDir}/{self.category}-{strpage}-{idx}.png'
                        #print (name)
                        image.save(name, mode='wb')
                    idx = idx + 1
            strpage=strpage+1
        doc.close()


    def parse_words(self):
        lines = {}
        doc = pymupdf.open(f"pdf/{self.filename}") # open a document
        block_size = 0
        for page in doc: # iterate the document pages
            words = (page.get_text("words", sort=False))
            for t in words:          
                l = t[4].rstrip()
                s = block_size + 10000 * int(t[1]/self._round)*self._round
                if len(l) > 0:
                    d = l.split('\n')
                    if len(d) > 1:
                        for e in d:
                            if s in lines:
                                lines[s]=lines[s]+' '+e 
                            else:
                                lines[s]=e 
                    else:
                        if s in lines:
                            lines[s]=lines[s]+' '+l
                        else:
                            lines[s]=l
            block_size = block_size + 10000000
        sorted_lines = dict(sorted(lines.items()))
        for k ,v in sorted_lines.items():
            self.lines.append(v)
        doc.close()
                  
    def parse_block(self):
        lines = {}
        doc = pymupdf.open(f"pdf/{self.filename}") # open a document
        block_size = 0
        for page in doc: # iterate the document pages
            text = (page.get_text("blocks", sort=False))
            for t in text:          
                l = t[4].rstrip()
                s = block_size + 10000 * t[1]
                skip_step = False
                for skip in self.pattern_skip:
                    match_obj = re.match(skip, l)
                    if match_obj:
                        skip_step = True
                        break
                if skip_step:
                    continue
                if len(l) > 0:
                    d = l.split('\n')
                    if len(d) > 1:
                        for e in d:
                            s = s + 1 
                            lines[s]=e 
                    else:
                        s = s + 1
                        lines[s]=l
            block_size = block_size + 10000000
        sorted_lines = dict(sorted(lines.items()))
        for k ,v in sorted_lines.items():
            self.lines.append(v)
        doc.close()

                                            
    def parse_dict(self):
        doc = pymupdf.open(f"pdf/{self.filename}") # open a document
        for page in doc: # iterate the document pages
            text = (page.get_text("dict", sort=False))
            for block in text['blocks']:
                if block['type'] == 0:
                    for line in block['lines']:
                        for span in line['spans']:
                            #print(span)
                            l = span['text'].rstrip()
                            skip_step = False
                            for skip in self.pattern_skip:
                                match_obj = re.match(skip, l)
                                if match_obj:
                                    skip_step = True
                                    break
                            if skip_step:
                                continue
                            if len(l) > 0:
                                self.lines.append(l)
        doc.close() 
                                        
    def format_answer(self, num):
        if num == 1:
            return "a"  
        if num == 2:
            return "b"  
        if num == 3:
            return "c"  
        if num == 4:
            return "d"  
        return "NONE"
    
    def format_remove(self, text, remove_str):
        text = text.strip()
        for s in remove_str:
            if text[:len(s)] == s:
                text = text[len(s):]
                continue 
        return text.strip()

    def format_remove_num(self, text, num):
        text_in = text.strip()
        remove_str = [str(num) + ' - ',str(num)+'. ']
        for s in remove_str:
            if text_in[:len(s)] == s:
                text_in = text_in[len(s):]
                continue
        return text_in.strip()       

    def make_image_hash(self, text):
        mapping = {'slici ':'slika ',
                   'sliku ':'slika ', 
                    ' ':'', 
                    '.':'',
                    '-':'',
                    '(':'', 
                    ')':''}
        text = text.lower()
        for k, v in mapping.items():
            text = text.replace(k, v)
        return text

    def writerow(self, writer):

        if len(self.str_q) == 0 and len(self.str_a) == 0 and len(self.str_b) == 0:
            return
        if len(self.str_a) == 0:
            self.error('answer a empty')
        if len(self.str_b) == 0:
            self.error('answer b empty')
        if len(self.str_q) > 0: 
            n = (self.q_number - 1)
            str_qq = self.format_remove_num(self.str_q, n)
            str_aa = self.format_remove(self.str_a, ['a.','1.','1)'])
            str_bb = self.format_remove(self.str_b, ['b.','2.','2)'])
            str_cc = self.format_remove(self.str_c, ['c.','3.','3)'])
            str_dd = self.format_remove(self.str_d, ['d.','4.','4)'])
            answer = 'a'
            img = None
            len_len = 0

            t = self.make_image_hash(str_qq)
            for image_name, image_path in self.slike.items():
                match = t.find(image_name)
                current_len = len(image_name)
                if match > 0 and len_len  < current_len:
                    img = image_path
                    len_len = current_len
                    self.question_to_images[image_path]=img

            if len(self.answer)>0:
                answer = self.answer[n]
                 
            writer.writerow({'number': n,'question': str_qq, 'a': str_aa ,'b': str_bb ,'c': str_cc ,'d': str_dd ,'right_answer': answer , 'category': self.category, 'img': img})
    
    def error(self, msg):
        print(f"! {msg} {self.filename}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")   
            
    def parse(self, csvfile):
        writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames, dialect='excel', delimiter = ';',  quotechar = '"', quoting=csv.QUOTE_ALL)
        i = 0
        while i < self.l_line:      
            i = i + 1
            l = self.lines[i]
            match_answere = re.match(self.pattern_answer, l)
            if match_answere:
                break
            skip_step = False
            for skip in self.pattern_skip:
                match_skip = re.match(skip, l)
                if match_skip:
                    skip_step = True
                    break
            if skip_step:
                continue
            match_tab = re.match(self.pattern_tab, l)
            if match_tab:
                self.error(self.pattern_tab)
            match_obj = re.match(self.pattern_q, l)
            if match_obj:
                self.writerow(writer)
                self.q_number = self.q_number + 1
                self.pattern_q = self.pattern_q_.replace('{number}',str(self.q_number))
                self.str_q = ""
                self.str_a = ""
                self.str_b = ""
                self.str_c = ""
                self.str_d = ""
                self.in_str  = "q"

            match_a = re.match(self.pattern_a, l)
            if match_a:
                self.in_str  = "a"
            match_b = re.match(self.pattern_b, l)
            if match_b:
                self.in_str  = "b"
            match_c = re.match(self.pattern_c, l)
            if match_c:
                self.in_str  = "c"
            match_d = re.match(self.pattern_d, l)
            if match_d:
                self.in_str  = "d"

            if self.in_str == "a":
                self.str_a = self.str_a + " " + l
            if self.in_str == "b":
                self.str_b = self.str_b + " " + l
            if self.in_str == "c":
                self.str_c = self.str_c + " " + l
            if self.in_str == "d":
                self.str_d = self.str_d + " " + l
            if self.in_str == "q":
                self.str_q = self.str_q + " " + l

        self.writerow(writer)
        if self.num_question != self.q_number - 1:
            self.error('num qestion not equal')
        if len(self.question_to_images)!= len(self.slike):
            self.error('img not equal')

          
