import instaloader
import tkinter as tk
from tkinter import messagebox


def dowlandPost():    #kullanıcı adını aldıgım yer
    username=entryUserName.get()

    try:
        #nesne oluştur
        bot=instaloader.Instaloader()

        #profil nesnesi oluşturma yeri
        profile=instaloader.Profile.from_username(bot.context,username)
        #kullanici gönderilerini aldığım yer
        posts=profile.get_posts()
        #gönderileri indirme
        
        for index,post in enumerate(posts,):
            bot.download_post(post,target=f"{profile.username}_{index}")
        #başarılı ise
        messagebox.showinfo("Başarılı","Gönderiler indirildi")
    except Exception as e:
        messagebox.showerror("HATA",str(e))

    
root=tk.Tk()
root.title("instagram Gönderi indirme botu")
root.geometry("300x200")

label=tk.Label(root,text="Kullanıcı adı: ")
label.pack(pady=10)

entryUserName=tk.Entry(root)
entryUserName.pack()

dowlandButton=tk.Button(root,text="Bilgileri indir",command=dowlandPost)
dowlandButton.pack()

root.mainloop()