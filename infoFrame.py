# infoFrame.py
from customtkinter import CTkScrollableFrame, CTkLabel

def create_info_frame(parent, width, height, corner_radius, frameBgcolor, frameFgcolor):
    info_frame = CTkScrollableFrame(parent, width=width, height=height, corner_radius=corner_radius,bg_color=frameBgcolor,fg_color=frameFgcolor)
    
    CTkLabel(info_frame, text="Application Info", wraplength=300, font=("Impact", 32)).pack(pady=20, padx=14, anchor="w")
    
    
    CTkLabel(info_frame,
             text="The Arc* Email Campaign Desktop Application is a powerful and user-friendly tool designed to manage and execute email marketing campaigns efficiently from a desktop environment. Built using Python and CustomTkinter, the application offers a clean, modern UI with multi-frame navigation for ease of use. It provides essential features for bulk emailing making it ideal for businesses, marketing professionals, and organizations aiming to streamline their email communication strategies.",
             wraplength=320, justify="left", font=("Sitka Banner", 17)).pack(pady=10, padx=16, anchor="w")
    
    CTkLabel(info_frame, text="Design & Devloped by:", wraplength=300, font=("Impact", 28)).pack(pady=20, padx=14, anchor="w")
    CTkLabel(info_frame,
             #text="Ankit kushwaha\nPiyush Pal\nDharmvir Sahani",#
             text="Dharmvir Sahani",
             wraplength=320, justify="left", font=("Sitka Banner", 18)).pack(pady=0, padx=16, anchor="w")
    
    CTkLabel(info_frame, text="⚠️ This Project was submitted to College ⚠️ \n  In MAY 2025",text_color="red3" ,wraplength=350, font=("Impact", 18)).pack(pady=69, padx=14, anchor="w")
    

    return info_frame
