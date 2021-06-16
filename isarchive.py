import sys
import zipfile

def is_archive(filename, buf=10485760):
   with open(filename,'rb') as file:
      while line := file.read(int(buf)):
         if b'\x50\x4b\x03\x04' in line:
            try:
               the_zip_file = zipfile.ZipFile(filename)
               ret = the_zip_file.testzip()
               if ret is None:
                  return "ZIP"
            except zipfile.BadZipFile:
               pass
            except OSError as err:
               if "Invalid argument" not in f"{err}":
                  print(filename)
                  raise
         if b'\x50\x4b\x05\x06' in line:
            try:
               the_zip_file = zipfile.ZipFile(filename)
               ret = the_zip_file.testzip()
               if ret is None:
                  return "ZIP"
            except zipfile.BadZipFile:
               pass
            except OSError as err:
               if "Invalid argument" not in f"{err}":
                  print(filename)
                  raise
         if b'\x50\x4b\x07\x08' in line:
            try:
               the_zip_file = zipfile.ZipFile(filename)
               ret = the_zip_file.testzip()
               if ret is None:
                  return "ZIP"
            except zipfile.BadZipFile:
               pass
            except OSError as err:
               if "Invalid argument" not in f"{err}":
                  print(filename)
                  raise
         if b'\x52\x61\x72\x21\x1A\x07\x00' in line:
            return "RAR"
         if b'\x52\x61\x72\x21\x1A\x07\x01\x00' in line:
            return "RAR"
         if b'\x75\x73\x74\x61\x72\x00\x30\x30' in line:
            return "TAR"
         if b'\x75\x73\x74\x61\x72\x20\x20\x00' in line:
            return "TAR"
         if b'\x37\x7A\xBC\xAF\x27\x1C' in line:
            return "7Z"
         if b'\x78\x61\x72\x21' in line:
            return "XAR"
         if len(line)>8:
            if b'\x50' in line[-8:]: # ZIP?
               file.seek(-8,1)
            elif b'\x52' in line[-8:]: # RAR?
               file.seek(-8,1)
            elif b'\x75' in line[-8:]: # TAR?
               file.seek(-8,1)
            elif b'\x37' in line[-8:]: # 7Z?
               file.seek(-8,1)
            elif b'\x78' in line[-8:]: # XAR?
               file.seek(-8,1)
   return False

def is_zippng(filename, buf=10485760):
   return True if is_archive(filename, buf)=="ZIP" else False

def is_rarjpg(filename, buf=10485760):
   return True if is_archive(filename, buf)=="RAR" else False

if __name__=="__main__":
   if len(sys.argv)<=1:
      print("pathfile [maxbuff]")
      sys.exit(0)
   elif len(sys.argv)==2:
      print(is_archive(sys.argv[1]))
   else:
      print(is_archive(sys.argv[1],sys.argv[2]))