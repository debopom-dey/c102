import dropbox
def upload_file(file_from, file_to):
    access_token = 'hVHo03gMIpoAAAAAAAAAAeiYe7IlTn1sHuVpoEBorke9Ru7JQMeAOc9K6BydJ_68'
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("Your id is uploaded to dropbox successfully")
def main():
    q1=input('Enter your name:')
    q2=input('Enter name of your father:')
    q3=input('Enter name of your mother:')
    q4=input('Enter your birthdate:')
    q5=input('Enter your nationality:')
    q6=input('Enter your gender:')
    with open('text.txt','w+') as f:
        f.writelines("Name:"+q1+'\n')
        f.writelines("Name of your father:"+q2+'\n')
        f.writelines("Name of your mother:"+q3+'\n')
        f.writelines("Name of your birthdate:"+q4+'\n')
        f.writelines("Nattionality:"+q5+'\n')
        f.writelines("Gender:"+q6+'\n')
    file_from = "text.txt"
    file_to = input("Enter the path which you want to upload on dropbox: ") 
    upload_file(file_from,file_to)
main()