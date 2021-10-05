import dropbox

class uploadData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self,file_from,file_to):
        files = dropbox.Dropbox(self.access_token)

        with open(file_from,'rb')as f:
            files.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.A5KOl9tN53IP3EKbCfcuty8GNBrsC4VDps1Q9m5-YLtdxLsLnCzl46gIGrTGn6p1VQ6B68iFtpioZFg-p_YAhnShWuu5FpQspCX7mgnrKfd5Igw3Qs9DH0LJ-vgdvVrAFJzpwmA'
    transferData = uploadData(access_token) 

    file_from = input("enter the file or folder you want to upload")
    file_to = input("enter the path of the dropbox")

    transferData.upload_files(file_from,file_to)
    print("file has been uploaded")

main()                  