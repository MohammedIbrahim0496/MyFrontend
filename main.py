import flet as ft
import os
import asyncio
import httpx
i=0
pl1=[]
pl2=[]
r=0


def main(page: ft.Page):
    async def go_h(e):
        await page.scroll_to(offset=0.0,duration=ft.Duration(milliseconds=300),curve=ft.AnimationCurve.EASE_IN_OUT)

    async def go_s(e):
        await page.scroll_to(offset=300.0,duration=ft.Duration(milliseconds=300),curve=ft.AnimationCurve.EASE_IN_OUT)

    async def go_p(e):
        await page.scroll_to(offset=670.0,duration=ft.Duration(milliseconds=300),curve=ft.AnimationCurve.EASE_IN_OUT)

    async def go_c(e):
        await page.scroll_to(offset=950.0,duration=ft.Duration(milliseconds=300),curve=ft.AnimationCurve.EASE_IN_OUT)

    # --- NAVIGATION BAR ---
    nav_bar = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            ft.Text("MOHAMMED IBRAHIM |  BCA STUDENT", weight=ft.FontWeight.BOLD,size=13, color=ft.Colors.WHITE,expand=1),
            ft.Row(
                spacing=20,
                controls=[
                    ft.TextButton("HOME", style=ft.ButtonStyle(color=ft.Colors.BLUE_400,icon_size=1),on_click=go_h,expand=1),
                    ft.TextButton("SKILLS", style=ft.ButtonStyle(color=ft.Colors.WHITE_70,icon_size=1),on_click=go_s,expand=1),
                    ft.TextButton("PROJECTS", style=ft.ButtonStyle(color=ft.Colors.WHITE_70,icon_size=1),on_click=go_p,expand=1),
                    ft.TextButton("EXPERIENCE", style=ft.ButtonStyle(color=ft.Colors.WHITE_70,icon_size=1),on_click=go_c,expand=1),
                    ft.TextButton("CONTACT", style=ft.ButtonStyle(color=ft.Colors.WHITE_70,icon_size=1),on_click=go_c,expand=1),
                ],expand=1
            )
        ],expand=1
    )
    async def x(e):
        print(e)
        await page.launch_url("https://www.linkedin.com/in/mohammed-ibrahim-6a0796389")
    async def y(e):
            print(e)
            await page.launch_url("https://github.com/MohammedIbrahim0496") 
    img=ft.Image(src="resume.png",expand=1,expand_loose=True)
    async def z(e):
            asyncio.create_task(page.push_route("/resume"))          
    # --- HERO / HEADER SECTION ---
    hero_section = ft.Container(
        padding=30,
        bgcolor="#1E293B",
        border_radius=15,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Column(
                    expand=True,
                    spacing=10,
                    controls=[
                        ft.Text("MOHAMMED IBRAHIM |  BCA STUDENT(Final Year)", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text("Building AI Frontend with Flet, Python, and Developing AI models to perform complex operation", size=15, color=ft.Colors.WHITE_70),
                        ft.Row(
                            spacing=10,
                            controls=[
                                ft.IconButton(icon=ft.Icons.LINK, icon_color=ft.Colors.BLUE_400, tooltip="LinkedIn",on_click= x,icon_size=30),
                                ft.IconButton(icon=ft.Icons.CODE, icon_color=ft.Colors.WHITE, tooltip="GitHub",on_click=y,icon_size=30),
                                ft.IconButton(icon=ft.Icons.DESCRIPTION, icon_color=ft.Colors.WHITE, tooltip="Resume",on_click=z,icon_size=30),
                            ]
                        )
                    ]
                ),
                ft.Container(
                    border=ft.Border.all(3, ft.Colors.BLUE_500),
                    shape=ft.BoxShape.CIRCLE,
                    content=ft.CircleAvatar(
                        radius=60,
                        foreground_image_src=r"ibrahim.png",
                    )
                )
            ]
        )
    )

    # --- TECH SKILLS SECTION ---
    def build_skill_card(name, icon_name):
        return ft.Container(
            width=120,
            height=140,
            padding=12,
            bgcolor="#1E293B",
            border_radius=12,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=8,
                controls=[
                    ft.Image(src=icon_name, height=64,width=64),
                    ft.Text(name, weight=ft.FontWeight.BOLD, size=13, color=ft.Colors.WHITE),
                    #ft.ProgressBar(value=percentage / 100, color=color, bgcolor=ft.Colors.WHITE10, height=6),
                    #ft.Text(f"{percentage}%", size=10, color=ft.Colors.WHITE_54)
                ]
            )
        )

    skills_grid = ft.Row(
        wrap=True,
        spacing=15,
        run_spacing=15,
        controls=[
            build_skill_card("Python", "py.png"),
            build_skill_card("Flet", "flett.png"),
            build_skill_card("NumPy", "num.png"),
            build_skill_card("Pandas", "pandas.png"),
            build_skill_card("MatplotLib", "matp.png"),
            build_skill_card("Fast API", "fast.png"),
            build_skill_card("Machine Learning", "mlear.png"),
            build_skill_card("Scikit Learn", "sk.png"),
            build_skill_card("Deep Learning", "dlear.png"),
            build_skill_card("PyTorch", "pytorch.png"),
            build_skill_card("PostgreSQL", "postg.png"),
            build_skill_card("GitHub", "git.png"),
        ]
    )
    def pageloader(t):
        asyncio.create_task(page.push_route(t))
    # --- SELECTED PROJECTS SECTION ---
    def build_project_card(title, description, tags, img_url,fun):
        return ft.Container(
            width=320,
            bgcolor="#1E293B",
            border_radius=12,
            padding=15,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Image(src=img_url, height=140, border_radius=8),
                    ft.Text(title, weight=ft.FontWeight.BOLD, size=16, color=ft.Colors.WHITE),
                    ft.Text(description, size=12, color=ft.Colors.WHITE_70, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Row(
                        spacing=8,
                        controls=[
                            ft.Chip(label=ft.Text(tag, size=10,color=ft.Colors.WHITE),color=ft.Colors.BLACK, bgcolor=ft.Colors.BLACK, height=24) for tag in tags
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Button("LIVE DEMO", style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE),on_click=lambda e:pageloader(fun)),
                            #ft.OutlinedButton("CODE", style=ft.ButtonStyle(color=ft.Colors.WHITE, side=ft.BorderSide(1, ft.Colors.WHITE38)))
                        ]
                    )
                ]
            )
        )
    projects_row = ft.Container(ft.Row(
        scroll=ft.ScrollMode.ALWAYS,
        spacing=20,
        controls=[
            build_project_card(
                "Calculator",
                "Learned creating UI.",
                ["Python", "Flet"],
                "calc.png","/calculator"
            ),
            build_project_card(
                "TIC TAC TOE",
                "Implemented an AI player as opponent.",
                ["Python", "Flet","Minmax"],
                "tic.png","/ticselect"
            ),
            build_project_card(
                "Diabetes Predictor",
                "Developed an ML model to predict the person is having diabetes or not.",
                ["Python", "Flet", "Scikit Learn"],
                "dib.png","/diab"
            ),
            build_project_card(
                "Vehicle Value Predictor",
                "An model that is capable of predicting the current value of owned vehicle.",
                ["Python", "Flet", "Scikit Learn"],
                "car.png","/vehicle"
            ),
            build_project_card(
                "Spam Email Detector",
                "An model that is capable of predicting whether an email is spam or not.",
                ["Python", "Flet", "Scikit Learn"],
                "spame.png","/spamd"
            ),
        ]
    ),
    )
    
    # --- EXPERIENCE SECTION ---
    def build_experience_item(role, company, period, bullets):
        return ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=15,
            controls=[
                ft.Container(
                    width=40,
                    height=40,
                    bgcolor=ft.Colors.BLUE_600,
                    shape=ft.BoxShape.CIRCLE,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Icon(ft.Icons.WORK, size=20, color=ft.Colors.WHITE)
                ),
                ft.Column(
                    spacing=5,
                    expand=True,
                    controls=[
                        ft.Text(f"{role} - {company}", weight=ft.FontWeight.BOLD, size=16, color=ft.Colors.WHITE),
                        ft.Text(period, size=12, color=ft.Colors.BLUE_400),
                        *[ft.Text(f"• {bullet}", size=13, color=ft.Colors.WHITE_70) for bullet in bullets]
                    ]
                )
            ]
        )

    experience_list = ft.Column(
        spacing=20,
        controls=[
            build_experience_item(
                "LEARNT DESIGNING UI(USER INTERFACE).",
                "OWN PROJECT",
                "JAN 2026 - FEB2026",
                [
                    "Build my first project calculator.",
                    "Build mt second project TIC-TAC-TOE With AI opponent."
                ]
            ),
            build_experience_item(
                "LEARNT MACHINE LEARNING AND BACKEND DEVELOPMENT",
                "OWN PROJECT",
                "FEB 2026 - MAT 2026",
                [
                    "Developed models that are capable of predicting the car price.",
                    "Developed models to predict wheather the patient have diabities or not.",
                    "Developed API and connected to frontend."
                ]
            )
        ]
    )

    sname=ft.TextField(value=None,label="Name", border_color=ft.Colors.WHITE_30, text_size=14)
    semail=ft.TextField(value=None,label="Email", border_color=ft.Colors.WHITE_30, text_size=14)
    smass=ft.TextField(value=None,label="Message", multiline=True,border_color=ft.Colors.WHITE_30, text_size=14,min_lines=4)
    status_text=ft.Text(value="",color=ft.Colors.TRANSPARENT)
    async def sendm():
        if sname.value==None or semail.value==None or smass.value==None:
            status_text.value ="Make Sure Every Feild Is filled"
            status_text.color="red"
            sname.value=None
            semail.value=None
            smass.value=None
        else:
            status_text.value ="Sending Email!!"
            status_text.color="yellow"
            page.update()
            await asyncio.sleep(1)
            x=[sname.value,semail.value,smass.value]
            try:
                status_text.value ="Sending Email!!"
                status_text.color="yellow"
                ans=httpx.post("https://mybackend-nipe.onrender.com/email",json=x,timeout=20.0)
                answ=ans.json()["email"]
                if answ ==0:
                    status_text.value ="Email Sent Succesfully!!"
                    status_text.color="green"
                    sname.value=None
                    semail.value=None
                    smass.value=None
                    page.update()
                else:    
                    status_text.value =f"{answ}Connection Errortttt \n Make Sure Every Feild Is filled"
                    status_text.color="red"
                    sname.value=None
                    semail.value=None
                    smass.value=None
                    page.update()
            except Exception as e:
                status_text.value =f"Connection Error \n Make Sure Your Are Connected To Internet"
                status_text.color="red"
                sname.value=None
                semail.value=None
                smass.value=None
                page.update()
            finally:
                await asyncio.sleep(4)    
                status_text.value =""
                status_text.color=ft.Colors.TRANSPARENT 
                page.update()   
    # --- CONTACT SECTION ---
    contact_form = ft.Container(
        padding=25,
        bgcolor="#1E293B",
        border_radius=12,
        content=ft.Column(
            spacing=15,
            controls=[
                ft.Text("CONTACT", weight=ft.FontWeight.BOLD, size=18, color=ft.Colors.WHITE),
                sname,
                semail,
                smass,
                status_text,
                ft.Button(
                    "Send Message",
                    style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE),
                    width=400,
                    height=45,on_click=sendm
                )
            ]
        )
    )
    #Spam
    email=ft.TextField(value=None,label="Enter Your Email",multiline=True,min_lines=5,expand=1,color="white",cursor_color="white",max_lines=10)
    ree=ft.Text(value="",color=ft.Colors.TRANSPARENT,size=22,weight=ft.FontWeight.BOLD)
    sb=ft.ProgressBar(value=0.0,expand=1,color="#FF0202")
    hb=ft.ProgressBar(value=0.0,expand=1,color="#08D220")
    ham=0.0
    spam=0.0
    async def chemail():
        ree.value=f"Detecting Spam In Email..."
        ree.color="#F7F304"
        page.update()
        await asyncio.sleep(1)
        try:    
            x=email.value
            spam=httpx.post("https://mybackend-nipe.onrender.com/spam",json=x,timeout=20.0)
            spam=spam.json()["prediction"]
            ham=1-spam
            if ham>spam:
                hb.value=ham
                sb.value=spam
                ree.value=f"Email Is Ham(NOT A SPAM) {spam*100:.2f}% SPAM DETECTED"
                ree.color="#00A80B"
            else:
                hb.value=ham
                sb.value=spam
                ree.value=f"Email Is SPAM (BE CAREFUL)  {spam*100:.2f}% SPAM DETECTED"
                ree.color="#FF0202"
            page.update()    
        except Exception as e:
            print(e)
            ree.value=f"Error Occured: {e} \n Make Sure Your Are Connected To Internet"
            ree.color="#FF0202"
            page.update()
        finally:
            await asyncio.sleep(5)
            email.value=None
            ree.value=""
            ree.color=ft.Colors.TRANSPARENT
            sb.value=0.0
            hb.value=0.0
            page.update()    
    ep= ft.Container(
        padding=30,
        bgcolor="#73D4F5",
        border_radius=15,
        expand=1,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    expand=True,
                    spacing=10,
                    controls=[
                        ft.Text("Spam", size=20, weight=ft.FontWeight.BOLD, color="#FF0202"),
                        sb,
                    ]
                ),
                ft.Row(
                    expand=True,
                    spacing=10,
                    controls=[
                        ft.Text("Ham ", size=20, weight=ft.FontWeight.BOLD, color="#196422"),
                        hb,
                    ]
                ),
            ]
        )
    )
    #Diabetes Predictor
    #
    tdt=ft.AlertDialog(title=ft.Text("AI Prediction"),content=ft.Text("You May Have Diabetes"),actions=[ft.TextButton("OK",on_click=lambda e:closedi(tdt))])
    tdf=ft.AlertDialog(title=ft.Text("AI Prediction"),content=ft.Text("You Dont Have Diabetes"),actions=[ft.TextButton("OK",on_click=lambda e:closedi(tdf))])
    tdk=ft.AlertDialog(title=ft.Text("ERROR"),content=ft.Text("Enter Only Numberic Value \n check your data connection \n Reload The Page After 1 Minute"),actions=[ft.TextButton("OK",on_click=lambda e:closedi(tdk))])
    def clickdiab():
        try:
            x=[float(pd.value),float(gd.value),float(bpd.value),float(sd.value),float(insd.value),float(bd.value),float(dd.value),float(ad.value)]
            ans=httpx.post("https://mybackend-nipe.onrender.com/predict",json=x,timeout=20.0)
            ans=ans.json()["prediction"]
            if ans == 1:
                page.clean()
                page.dialog=tdt
                tdt.open=True 
                page.add(tdt)    
                page.update()
                pd.value=0
                gd.value=""
                bpd.value=""
                sd.value=""
                insd.value=""
                bd.value=""
                dd.value=""
                ad.value=""
                button.disabled=True
                page.add(
                        ft.Column([
                            ft.Button('Back To MainPage',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/"))
                        ]),
                        ft.Column([pd,gd,bpd,sd,insd,bd,dd,ad,buttondd,]))
                page.update()
            else:
                page.clean()
                page.dialog=tdf
                tdf.open=True 
                page.add(tdf)    
                page.update()
                pd.value=0
                gd.value=""
                bpd.value=""
                sd.value=""
                insd.value=""
                bd.value=""
                dd.value=""
                ad.value=""
                button.disabled=True
                page.add(
                        ft.Column([
                            ft.Button('Back To MainPage',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/"))
                        ]),
                        ft.Column([pd,gd,bpd,sd,insd,bd,dd,ad,buttondd,]))
                page.update()
        except :
            page.clean()
            page.dialog=tdk
            tdk.open=True 
            page.add(tdk)    
            page.update()
            pd.value=0
            gd.value=""
            bpd.value=""
            sd.value=""
            insd.value=""
            bd.value=""
            dd.value=""
            ad.value=""
            button.disabled=True
            page.add(
                    ft.Column([
                        ft.Button('Back To MainPage',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/"))
                    ]),
                    ft.Column([pd,gd,bpd,sd,insd,bd,dd,ad,buttondd,]))
            page.update()        
    def closedi(e):
        e.open=False
        page.update() 
    async def f1d():
        await gd.focus()
    async def f2d():
        await bpd.focus()
    async def f3d():
        await sd.focus()
    async def f4d():
        await bd.focus()
    async def f5d():
        await dd.focus() 
    async def f6d():
        await ad.focus()
    async def f7d():
        await insd.focus()
    def f8d():
        clickdiab()          
    pd=ft.TextField(label="Pregnancies",expand=1,value=0,on_change=lambda e:v(),autofocus=True)    
    gd=ft.TextField(label="Glucose",expand=1,on_change=lambda e:v())
    bpd=ft.TextField(label="BloodPressure",expand=1,on_change=lambda e:v())
    sd=ft.TextField(label="SkinThickness",expand=1,on_change=lambda e:v())
    bd=ft.TextField(label="BMI",expand=1,on_change=lambda e:v())
    dd=ft.TextField(label="DiabetesPedigreeFunction",expand=1,on_change=lambda e:v())
    ad=ft.TextField(label="Age",expand=1,on_change=lambda e:v())
    insd=ft.TextField(label="Insulin",expand=1,on_change=lambda e:v())
    pd.on_submit=lambda e:e.page.run_task(f1d)
    gd.on_submit=lambda e:e.page.run_task(f2d)
    bpd.on_submit=lambda e:e.page.run_task(f3d)
    sd.on_submit=lambda e:e.page.run_task(f7d)
    bd.on_submit=lambda e:e.page.run_task(f5d)
    dd.on_submit=lambda e:e.page.run_task(f6d)
    ad.on_submit=lambda e:f8d()
    insd.on_submit=lambda e:e.page.run_task(f4d)
    buttondd=ft.Button("Predict",bgcolor="blue",color="white",width=300,disabled=True,on_click=clickdiab)
    def v():
        if pd.value!= "" and gd.value!= "" and bpd.value!= "" and sd.value!= "" and insd.value!= "" and bd.value!= "" and dd.value!= "" and ad.value != "":
            buttondd.disabled=False
            page.update()
        else:
            buttondd.disabled=True
            page.update()
        page.update()
    #Vehicle Price Predictor
    opt=["City","Corolla Altis","Verna","Fortuner","Brio","Ciaz","i20","Innova","Grand i10",
        "Royal Enfield Classic 350","Amaze","Jazz","eon","sx4","Ertiga","Swift","Alto k10",
        "i10","Drize","Royal Enfield Thunder 350","Etios Liva","Wagon R","Bajaj Pulsur 150",
        "Ritz","Honda CB Hornet 160R","Bajaj Avenger 220","Yamaha FZ5 v2.0","Xcent","Bajaj Pulsur NS 200",
        "TVS Apache RTR 160","Etios Cross","Etios G","Royal Enfield Thunder 500","Creta","Honda CB Shine","Honda Activa",
        "Activa","Activa 3G","Activa 4G","Activa 5G","Activa 6G","Bajaj Discover 125","Elantra",
        "Honda Karizma","Honda CB Twister","Hero Extreme","Honda CBR 150","Yamaha FZ v2.0",
        "Bajaj Avenger 220 dtsi","Hero Passion Pro","Hero Splendor ISmart","TVS Apache RTR 180",
        "Bajaj Pulsur 200 F","Royal Enfield Classic 500","KTM RC 390","Hyosung GT 250 R",
        "KTM RC 200","Bajaj Dominar 400","UM Renegade Mojave","Etios GD","Camry","Land Crusier",
        "Corolla","S Cross","Vitara Brezza","Alto 800","Baleno","Ignis","Omni","KTM 390 Duke",
        "Bajaj Pulsur 135 LS","Honda CB Trigger","Yamaha FZ5","Bajaj Avenger Street 220","Bajaj Pulsur NS 400","Yamaha Frazer",
        "Honda Dream Yuga","Hero Passion X Pro","Mahindra Mojo XT 300","Bajaj Pulsur RS 200",
        "Royal Enfield Bullet 350","Bajaj Avenger 150 Street","Bajaj Avenger 150","Yamaha FZ 16",
        "TVS Sport","Hero Super Splendor","Hero Glamour","Suzuki Access 125","TVS Wego","Hero Honda Passion Pro",
        "Bajaj Discover 100","Activa 125","TVS Jupyter","Hero Splendor Plus","Hero CBZ Extreme",
        "Hero CB Unicorn","Hero Hunk","Bajaj CT 100","Hero Ingnitor Disc"]
    def clickveh():
        try:
            if f.value ==3:
                f.value=0
            be=float(bp.value) /100000    
            x=[int(g.value),float(be),float(s.value),int(f.value),int(se.value),int(tr.value),int(ow.value)]
            ans=httpx.post("https://mybackend-nipe.onrender.com/carpredict",json=x,timeout=20.0)
            ans=ans.json()["prediction"]
            if be<=4.0:
                answer=int(ans*10000)
            else :
                answer=int(ans*100000)    
            if ca.value != "":
                tt=ft.AlertDialog(title=ft.Text("AI Prediction"),content=ft.Text(f"Your \"{ca.value}\" Value Can Be Around \n Rupees :  {answer}"),actions=[ft.TextButton("OK",on_click=lambda e:closeveh(tt))])
            else:
                tt=ft.AlertDialog(title=ft.Text("AI Prediction"),content=ft.Text(f"Your Vehicle Value Can Be Around \n Rupees :  {answer}"),actions=[ft.TextButton("OK",on_click=lambda e:closeveh(tt))])
            page.clean()
            page.dialog=tt
            tt.open=True 
            page.add(tt)    
            page.update()
            ca.value=""
            g.value=""
            bp.value=""
            s.value=""
            f.value=None
            se.value=None
            tr.value=None
            ow.value=None
            button.disabled=True
            page.add(
                    ft.Column([
                        ft.Button('Back To MainPage',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/"))
                    ]),
                    ft.Container(content=ft.Text("Vehicle Name (Optional)"),alignment=ft.Alignment.TOP_LEFT),
                    ft.Column([ca,g,bp,s,b,d,a,ind,button,]))
            page.update()
        except Exception as e:
            if e == "The read operation timed out":
                tk=ft.AlertDialog(title=ft.Text("ERROR"),content=ft.Text(f"{e}\n Check your data connection \n And Try Reloading After 1 Minute"),actions=[ft.TextButton("OK",on_click=lambda e:closeveh(tk))])
            else:
                tk=ft.AlertDialog(title=ft.Text("ERROR"),content=ft.Text(f"{e}\n Make Sure You Have Filled All Needed Thing \n And The Year,Kilometer,Price Must Be Numeric \n And Try Reloading After 1 Minute"),actions=[ft.TextButton("OK",on_click=lambda e:closeveh(tk))])
            page.clean()
            page.dialog=tk
            tk.open=True 
            page.add(tk)    
            page.update()
            ca.value=""
            g.value=""
            bp.value=""
            s.value=""
            f.value=None
            se.value=None
            tr.value=None
            ow.value=None
            button.disabled=True
            page.add(
                    ft.Column([
                        ft.Button('Back To MainPage',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/"))
                    ]),
                    ft.Container(content=ft.Text("Vehicle Name (Optional)"),alignment=ft.Alignment.TOP_LEFT),
                    ft.Column([ca,g,bp,s,b,d,a,ind,button,]))
            page.update()      
    def closeveh(e):
        e.open=False
        page.update() 
    async def f1():
        await g.focus()
    async def f2():
        await bp.focus()
    async def f3():
        await s.focus() 
    f=ft.RadioGroup(
                content=ft.Column([
                    ft.Radio(value=0,label="Petrol",),
                    ft.Radio(value=1,label="Diesel"),
                    ft.Radio(value=2,label="CNG"),
                    ft.Radio(value=3,label="Electric")
                ]),
            ) 
    se=ft.RadioGroup(
                content=ft.Column([
                    ft.Radio(value=0,label="Dealer",),
                    ft.Radio(value=1,label="Individual"),
                ]),
            )  
    tr=ft.RadioGroup(
                content=ft.Column([
                    ft.Radio(value=0,label="Manual",),
                    ft.Radio(value=1,label="Automatic"),
                ]),
            )   
    ow=ft.RadioGroup(
                content=ft.Column([
                    ft.Radio(value=0,label="First Owner",),
                    ft.Radio(value=1,label="Second Owner"),
                    ft.Radio(value=2,label="Third Owner"),
                    ft.Radio(value=3,label="Fourth Owner")
                ]),
            ) 
    sugg=[ft.AutoCompleteSuggestion(key=f,value=f)for f in opt]        
    ca=ft.AutoComplete(suggestions=sugg,on_select=lambda e:ve(e))
    g=ft.TextField(label="Manufactured Year *",expand=1,on_change=lambda e:v(),color=ft.Colors.WHITE,)
    bp=ft.TextField(label="Purchased Price *",expand=1,on_change=lambda e:v())
    s=ft.TextField(label="Kilo-Meters Driven *",expand=1,on_change=lambda e:v())
    b=ft.Container(ft.Column([ft.Text("Fuel Type *"),f]))
    d=ft.Container(ft.Column([ft.Text("Seller Type *"),se]))
    a=ft.Container(ft.Column([ft.Text("Transmission *"),tr]))
    ind=ft.Container(ft.Column([ft.Text("Number Of Owners *"),ow]))
    ca.on_submit=lambda e:e.page.run_task(f1)
    g.on_submit=lambda e:e.page.run_task(f2)
    bp.on_submit=lambda e:e.page.run_task(f3)
    button=ft.Button("Predict",bgcolor="blue",color="white",width=300,disabled=True,on_click=clickveh)
    cname=ft.TextField()
    def v():
        if g.value!= "" and bp.value!= "" and s.value!= "":
            button.disabled=False
            page.update()
        else:
            button.disabled=True
            page.update()
            rcol=ft.Column(spacing=0)
    def ve(e:ft.AutoCompleteSelectEvent):
        cname.value=e.selection.value
        page.update()              
    page.update()
    #TIC TAC TOE
    #
    global i, pl1, pl2, r
    radiotic=ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value=1,label="With Unbeatable AI",fill_color=ft.Colors.WHITE,label_style=ft.TextStyle(color=ft.Colors.WHITE)),
            ft.Radio(value=2,label="With Friend",fill_color=ft.Colors.WHITE,label_style=ft.TextStyle(color=ft.Colors.WHITE))
        ]),
    )
    t11=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic1click(t11,"1"))
    t12=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic1click(t12,"2"))
    t13=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic1click(t13,"3"))
    t14=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic1click(t14,"4"))
    t15=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic1click(t15,"5"))
    t16=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic1click(t16,"6"))
    t17=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic1click(t17,"7"))
    t18=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic1click(t18,"8"))
    t19=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic1click(t19,"9"))
    t1a=ft.AlertDialog(title=ft.Text("ALERT"),content=ft.Text("AI Wins"),actions=[ft.TextButton("OK",on_click=lambda e:close1(t1a))])    
    t1t=ft.AlertDialog(title=ft.Text("ALERT"),content=ft.Text("X Wins"),actions=[ft.TextButton("OK",on_click=lambda e:close1(t1t))])
    t1f=ft.AlertDialog(title=ft.Text("ALERT"),content=ft.Text("O Wins"),actions=[ft.TextButton("OK",on_click=lambda e:close1(t1f))])
    t1k=ft.AlertDialog(title=ft.Text("ALERT"),content=ft.Text("Draw"),actions=[ft.TextButton("OK",on_click=lambda e:close1(t1k))])
    t01=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic0click(t01,"1"))
    t02=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic0click(t02,"2"))
    t03=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic0click(t03,"3"))
    t04=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic0click(t04,"4"))
    t05=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic0click(t05,"5"))
    t06=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic0click(t06,"6"))
    t07=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic0click(t07,"7"))
    t08=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic0click(t08,"8"))
    t09=ft.Button("",color="white",margin=ft.Margin.symmetric(vertical=10,horizontal=10),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),width=100,height=100,on_click=lambda e:tic0click(t09,"9"))
    ta=ft.AlertDialog(title=ft.Text("ALERT"),content=ft.Text("AI Wins"),actions=[ft.TextButton("OK",on_click=lambda e:close(ta))])    
    tt=ft.AlertDialog(title=ft.Text("ALERT"),content=ft.Text("X Wins"),actions=[ft.TextButton("OK",on_click=lambda e:close(tt))])
    tf=ft.AlertDialog(title=ft.Text("ALERT"),content=ft.Text("O Wins"),actions=[ft.TextButton("OK",on_click=lambda e:close(tf))])
    tk=ft.AlertDialog(title=ft.Text("ALERT"),content=ft.Text("Draw"),actions=[ft.TextButton("OK",on_click=lambda e:close(tk))])
    def tic1click(e, b):
        global i, pl1, pl2, r
        pl1.append(b)
        e.disabled=True
        e.content=ft.Text("X",size=70,weight="bold",italic=True,color="white")
        page.update()
        i +=1
        if win(pl1):
            i=0
            page.clean()
            pl1.clear()
            pl2.clear()
            t11.content=("")
            t11.disabled=False
            t12.content=("")
            t12.disabled=False  
            t13.content=("")
            t13.disabled=False  
            t14.content=("")
            t14.disabled=False  
            t15.content=("")
            t15.disabled=False  
            t16.content=("")
            t16.disabled=False 
            t17.content=("")
            t17.disabled=False  
            t18.content=("")
            t18.disabled=False  
            t19.content=("")
            t19.disabled=False
            
            page.add(ft.Column([
                            ft.Column([
                                        ft.Button('Back To Player Selection Page',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/ticselect"))
                                    ]),
                            ft.Row([t11,t12,t13]),
                            ft.Row([t14,t15,t16]),
                            ft.Row([t17,t18,t19]),
                        ]),)
            page.dialog=t1t
            t1t.open=True 
            page.add(t1t)
            page.update()
        if i!=9:  
            b = str(best_score(pl1,pl2))
            if b=="1":
                t11.disabled=True
                t11.content=ft.Text("O",size=70,weight="bold",italic=True,color="white")
                page.update()
            elif b=="2":
                t12.disabled=True
                t12.content=ft.Text("O",size=70,weight="bold",italic=True,color="white")
                page.update()
            elif b=="3":
                t13.disabled=True
                t13.content=ft.Text("O",size=70,weight="bold",italic=True,color="white")
                page.update()
            elif b=="4":
                t14.disabled=True
                t14.content=ft.Text("O",size=70,weight="bold",italic=True,color="white")
                page.update()
            elif b=="5":
                t15.content=ft.Text("O",size=70,weight="bold",italic=True,color="white")
                t15.disabled=True
                page.update()

            elif b=="6":
                t16.disabled=True
                t16.content=ft.Text("O",size=70,weight="bold",italic=True,color="white")
                page.update()
            elif b=="7":
                t17.disabled=True
                t17.content=ft.Text("O",size=70,weight="bold",italic=True,color="white")
                page.update()
            elif b=="8":
                t18.disabled=True
                t18.content=ft.Text("O",size=70,weight="bold",italic=True,color="white")
                page.update()
            else:
                e=t19
                t19.disabled=True
                t19.content=ft.Text("O",size=70,weight="bold",italic=True,color="white") 
                page.update()         
            pl2.append(b)
            page.update()
            i+=1
            if win(pl2):
                i=0
                page.clean()
                pl1.clear()
                pl2.clear()
                t11.content=("")
                t11.disabled=False
                t12.content=("")
                t12.disabled=False  
                t13.content=("")
                t13.disabled=False  
                t14.content=("")
                t14.disabled=False  
                t15.content=("")
                t15.disabled=False  
                t16.content=("")
                t16.disabled=False 
                t17.content=("")
                t17.disabled=False  
                t18.content=("")
                t18.disabled=False  
                t19.content=("")
                t19.disabled=False
                page.add(ft.Column([
                                ft.Column([
                                            ft.Button('Back To Player Selection Page',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/ticselect"))
                                        ]),
                               ft.Row([t11,t12,t13]),
                               ft.Row([t14,t15,t16]),
                               ft.Row([t17,t18,t19]),
                            ]),)
                page.dialog=t1f
                t1f.open=True 
                page.add(t1f)
                page.update()         
        if i==9:
            i=0
            page.clean()
            pl1.clear()
            pl2.clear()
            t11.content=("")
            t11.disabled=False
            t12.content=("")
            t12.disabled=False  
            t13.content=("")
            t13.disabled=False  
            t14.content=("")
            t14.disabled=False  
            t15.content=("")
            t15.disabled=False  
            t16.content=("")
            t16.disabled=False 
            t17.content=("")
            t17.disabled=False  
            t18.content=("")
            t18.disabled=False  
            t19.content=("")
            t19.disabled=False
            page.add(ft.Column([
                            ft.Column([
                                        ft.Button('Back To Player Selection Page',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/ticselect"))
                                    ]),
                            ft.Row([t11,t12,t13]),
                            ft.Row([t14,t15,t16]),
                            ft.Row([t17,t18,t19]),
                        ]),)
            page.dialog=t1k
            t1k.open=True 
            page.add(t1k)
            page.update()
    def tic0click(e, b):
        global i, pl1, pl2, r
        if i%2==0:
            pl1.append(b)
            e.disabled=True
            e.content=ft.Text("X",size=70,weight="bold",italic=True,color="white")
            page.update()
            i +=1
            if win(pl1):
                i=0
                page.clean()
                pl1.clear()
                pl2.clear()
                t01.content=("")
                t01.disabled=False
                t02.content=("")
                t02.disabled=False  
                t03.content=("")
                t03.disabled=False  
                t04.content=("")
                t04.disabled=False  
                t05.content=("")
                t05.disabled=False  
                t06.content=("")
                t06.disabled=False 
                t07.content=("")
                t07.disabled=False  
                t08.content=("")
                t08.disabled=False  
                t09.content=("")
                t09.disabled=False
                page.add(ft.Column([
                                ft.Column([
                                            ft.Button('Back To Player Selection Page',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/ticselect"))
                                        ]),
                                ft.Row([t01,t02,t03]),
                                ft.Row([t04,t05,t06]),
                                ft.Row([t07,t08,t09]),
                            ]),)
                page.dialog=tt
                tt.open=True 
                page.add(tt)
                page.update()
                
        else:
            pl2.append(b)
            e.disabled=True
            e.content=ft.Text("O",size=70,weight="bold",italic=True,color="white")
            page.update()
            i+=1
            if win(pl2):
                page.clean()
                i=0
                pl1.clear()
                pl2.clear()
                t01.content=("")
                t01.disabled=False
                t02.content=("")
                t02.disabled=False  
                t03.content=("")
                t03.disabled=False  
                t04.content=("")
                t04.disabled=False  
                t05.content=("")
                t05.disabled=False  
                t06.content=("")
                t06.disabled=False 
                t07.content=("")
                t07.disabled=False  
                t08.content=("")
                t08.disabled=False  
                t09.content=("")
                t09.disabled=False
                page.add(ft.Column([
                                ft.Column([
                                            ft.Button('Back To Player Selection Page',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/ticselect"))
                                        ]),
                                ft.Row([t01,t02,t03]),
                                ft.Row([t04,t05,t06]),
                                ft.Row([t07,t08,t09]),
                            ]),)
                page.dialog=tf
                tf.open=True 
                page.add(tf)
                page.update()         
        if i==9:
            i=0
            page.clean()
            pl1.clear()
            pl2.clear()
            t01.content=("")
            t01.disabled=False
            t02.content=("")
            t02.disabled=False  
            t03.content=("")
            t03.disabled=False  
            t04.content=("")
            t04.disabled=False  
            t05.content=("")
            t05.disabled=False  
            t06.content=("")
            t06.disabled=False 
            t07.content=("")
            t07.disabled=False  
            t08.content=("")
            t08.disabled=False  
            t09.content=("")
            t09.disabled=False
            page.add(ft.Column([
                            ft.Column([
                                        ft.Button('Back To Player Selection Page',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/ticselect"))
                                    ]),
                            ft.Row([t01,t02,t03]),
                            ft.Row([t04,t05,t06]),
                            ft.Row([t07,t08,t09]),
                        ]),)
            page.dialog=tk
            tk.open=True 
            page.add(tk)
            page.update()
    def close1(e):
        e.open=False
        asyncio.create_task(page.push_route("/ticai")) 
        page.update()   
    def close(e):
        e.open=False
        asyncio.create_task(page.push_route("/tichu"))
        page.update()
    def closet(e):
            e.open=False
            asyncio.create_task(page.push_route("/ticselect"))
            page.update()    
    def minmax(p1,p2,check):
        if win(p1): return-1
        if win(p2): return 1
        if len(p1)+len(p2) ==9: return 0
        tar =[str(n)for n in range(1,10)if str(n) not in p1 and str(n) not in p2]
        if check:
                best = -10
                for n in tar:
                    score =minmax(p1,p2+[n],False)
                    best =max(score,best)
                return best
        else:
                best = 10
                for n in tar:
                    score =minmax(p1+[n],p2,True)
                    best =min(score,best)
                return best
    def best_score(p1,p2):
        tar =[str(n)for n in range(1,10)if str(n) not in p1 and str(n) not in p2]
        move = ""
        best =-10
        for n in tar:
                score =minmax(p1,p2+[n],False)
                if score > best:
                    best = score
                    move = n
        return move
    def win(pl1):
        if '1' in pl1 and '2' in pl1 and '3' in pl1   :   
                return True
        if '4' in pl1 and '5' in pl1 and '6' in pl1   :   
                return True
        if '7' in pl1 and '8' in pl1 and '9' in pl1   :   
                return True
        if '1' in pl1 and '4' in pl1 and '7' in pl1   :   
                return True
        if '2' in pl1 and '5' in pl1 and '8' in pl1   :   
                return True
        if '3' in pl1 and '6' in pl1 and '9' in pl1   :   
                return True
        if '1' in pl1 and '5' in pl1 and '9' in pl1   :   
                return True
        if '3' in pl1 and '5' in pl1 and '7' in pl1   :   
                return True
        return False
    def cc():
            global r,i
            i=0
            pl1.clear()
            pl2.clear()
            try:
                r=int(radiotic.value)   
                if r==1:
                    asyncio.create_task(page.push_route("/ticai"))
                else:
                    asyncio.create_task(page.push_route("/tichu"))
            except:
                tt=ft.AlertDialog(title=ft.Text("ALERT"),content=ft.Text("Select Player Mode"),actions=[ft.TextButton("OK",on_click=lambda e:closet(tt))])
                page.dialog=tt
                tt.open=True 
                page.add(tt) 
    # Calculator
    #            
    def calclick (t):
        if t == "=":
            try:
                r = eval(x.value)
                x.value=str(r)
                total.value=""
                total.update()
            except:
                x.value="some error occured restart" 
                x.update()   
        elif t == "c" :
            c = x.value
            if len(c)>0 :
                x.value=x.value[:-1]
                x.update()
                total.value=""  
                total.update() 
            else:
                pass    
        elif t == "ac" :
            x.value=""
            x.update()
            total.value=""
            total.update()       
        else :
            c = x.value
            x.value=(str(c)+str(t))
            x.update()
            if t =="+" or t =="-" or t =="*" or t =="/" or t =="//" or t =="%"  :
                pass 
            else:
                try:
                    r = eval(x.value)
                    total.value=str(r)
                    total.update()
                except:
                    if t=="0" or t==".":
                        pass
                    else:
                        total.value="some error occured restart" 
                        total.update()
        page.update()                
    x = ft.TextField(align=ft.Alignment.BOTTOM_CENTER,bgcolor="grey",color="white",expand=1,text_size=30)
    total = ft.TextField(content_padding=0,align=ft.Alignment.BOTTOM_CENTER,bgcolor="grey",color="white",expand=1)
    ##Main loading
    #
    def navigate(route: str):
        asyncio.create_task(page.push_route(route))
    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()

        if page.route == "/calculator":
            page.title="Calculator"
            page.theme_mode=ft.ThemeMode.DARK
            page.views.append(
                ft.View(
                    route="/calculator",
                    controls=[
                            ft.Column([
                                ft.Button('Back To MainPage',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/"))
                            ]),
                            ft.Column([x,
                            total,]),
                            
                            ft.Row([
                                ft.Button('AC',bgcolor="blue",color="white", on_click=lambda e:calclick('ac'),expand=1),
                                ft.Button('//',bgcolor="grey",color="white", on_click=lambda e:calclick('//') ,expand=1),
                                ft.Button('%',bgcolor="grey",color="white", on_click=lambda e:calclick('%') ,expand=1),
                                ft.Button('/',bgcolor="grey",color="white", on_click=lambda e:calclick('/'),expand=1 ),
                                ]),
                            ft.Row([
                                ft.Button('7',bgcolor="grey",color="white", on_click=lambda e:calclick('7'),expand=1 ),
                                ft.Button('8',bgcolor="grey",color="white", on_click=lambda e:calclick('8'),expand=1 ),
                                ft.Button('9',bgcolor="grey",color="white", on_click=lambda e:calclick('9'),expand=1 ),
                                ft.Button('*',bgcolor="grey",color="white", on_click=lambda e:calclick('*'),expand=1 ),
                                ]),
                            ft.Row([
                                ft.Button('4',bgcolor="grey",color="white", on_click=lambda e:calclick('4'),expand=1 ),
                                ft.Button('5',bgcolor="grey",color="white", on_click=lambda e:calclick('5') ,expand=1),
                                ft.Button('6',bgcolor="grey",color="white", on_click=lambda e:calclick('6') ,expand=1),
                                ft.Button('-',bgcolor="grey",color="white", on_click=lambda e:calclick('-') ,expand=1),
                                ]),
                            ft.Row([
                                ft.Button('1',bgcolor="grey",color="white", on_click=lambda e:calclick('1'),expand=1),
                                ft.Button('2',bgcolor="grey",color="white", on_click=lambda e:calclick('2') ,expand=1),
                                ft.Button('3',bgcolor="grey",color="white", on_click=lambda e:calclick('3') ,expand=1),
                                ft.Button('+',bgcolor="grey",color="white", on_click=lambda e:calclick('+') ,expand=1),
                                ]),
                            ft.Row([
                                ft.Button('C',bgcolor="red",color="white", on_click=lambda e, x='c':calclick(x),expand=1),
                                ft.Button('0',bgcolor="grey",color="white", on_click=lambda e, x='0':calclick(x) ,expand=1),
                                ft.Button('.',bgcolor="grey",color="white", on_click=lambda e ,x='.':calclick(x) ,expand=1),
                                ft.Button('=',bgcolor="orange",color="white", on_click=lambda e, x='=':calclick(x) ,expand=1),
                                ]),    
                            ft.Text(value="\"%\" returns reminder \n \"//\" returns floor value of quotient",color="white",size=20,align=ft.Alignment.BOTTOM_CENTER),
                    ],
                )
            )
        elif page.route == "/tichu":
            page.title="Tic Tac Toe"
            page.views.append(
                ft.View(
                    route="/tichu",
                    controls=[ft.Column([
                    ft.Column([
                                ft.Button('Back To Player Selection Page',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/ticselect"))
                            ]),
                    ft.Row([t01,t02,t03]),
                    ft.Row([t04,t05,t06]),
                    ft.Row([t07,t08,t09]),
                ]),
                    ],
                )
            )
        elif page.route == "/ticai":
            page.title="Tic Tac Toe With AI"
            page.views.append(
                ft.View(
                    route="/ticai",
                    controls=[ft.Column([
                    ft.Column([
                                ft.Button('Back To Player Selection Page',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/ticselect"))
                            ]),
                    ft.Row([t11,t12,t13]),
                    ft.Row([t14,t15,t16]),
                    ft.Row([t17,t18,t19]),
                ]),
                    ],
                )
            )
        elif page.route == "/ticselect":
            page.title="Tic Tac Toe Player Selection"
            page.views.append(
                ft.View(
                    route="/ticselect",
                    controls=[
                ft.Column([
                    ft.Button('Back To MainPage',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/"))
                ]),
                radiotic,
                ft.Button("SUBMIT",bgcolor="blue",width=300,align=ft.Alignment.CENTER,on_click=cc)
                    ],
                )
            ) 
        elif page.route == "/diab":
            page.title="Diabetes Predictor"
            page.views.append(
                ft.View(
                    route="/diab",
                    controls=[
                    ft.Column([
                        ft.Button('Back To MainPage',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/"))
                    ]),
                    ft.Column([pd,gd,bpd,sd,insd,bd,dd,ad,buttondd,])
                    ],
                )
            )
        elif page.route == "/vehicle":
            page.title="Vehicle Price Predictor"
            page.theme_mode=ft.ThemeMode.DARK
            page.views.append(
                ft.View(
                    route="/vehicle",
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                    ft.Column([
                        ft.Button('Back To MainPage',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/"))
                    ]),
                    ft.Container(content=ft.Text("Vehicle Name (Optional)"),alignment=ft.Alignment.TOP_LEFT),
                    ft.Column([ca,g,bp,s,b,d,a,ind,button,])
                    ],
                )
            )
        elif page.route == "/resume":
            page.title="Mohammed Ibrahim Resume"
            page.views.append(
                ft.View(
                    route="/resume",
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                ft.Column([
                    ft.Button('Back To MainPage',bgcolor="blue",color="white",expand=1, on_click=lambda e:navigate("/")),img
                ]),
                    ],
                )
            )     
        elif page.route == "/spamd":
            page.title="Spam Email Detector"
            page.views.append(
                ft.View(
                    route="/spamd",
                    scroll=ft.ScrollMode.AUTO,
                    controls=[ft.Column(
            controls=[ft.Button("Back To Main Page",color="white",bgcolor="blue",on_click=lambda e:navigate("/")),
                email,
                ft.Button("Submit",color="white",bgcolor="blue",on_click=chemail),
                ree,
                ep])
                    ],
                )
            )                                                       
        else:
            page.title="Mohammed Ibrahim Portfolio"
            page.theme_mode=ft.ThemeMode.DARK
            page.views.append(
                ft.View(
                    route="/",
                    scroll=ft.ScrollMode.AUTO,
                    controls=[nav_bar,
                              ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                                hero_section,
                                ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
                                
                                ft.Text("TECH SKILLS", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                                skills_grid,
                                ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
                                
                                ft.Text("SELECTED PROJECTS", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                                projects_row,
                                ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
                                
                                ft.Row(
                                    vertical_alignment=ft.CrossAxisAlignment.START,
                                    spacing=30,
                                    controls=[
                                        ft.Column(
                                            expand=1,
                                            controls=[
                                                ft.Text("EXPERIENCE", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                                                experience_list
                                            ]
                                        ),
                                        ft.Column(
                                            expand=1,
                                            controls=[
                                                contact_form
                                            ]
                                        )
                                    ]
                                ),
                                ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                                ft.Container(
                                    alignment=ft.Alignment.CENTER,
                                    content=ft.Text("© 2026 Mohammed Ibrahim | Built with Flet", size=12, color=ft.Colors.WHITE_38)
                                ),
                    ],
                )
            )

        page.update()

    async def view_pop(e: ft.ControlEvent):
        if e.view is not None:
            page.views.remove(e.view)
            await page.push_route(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change(None)


ft.run(main)