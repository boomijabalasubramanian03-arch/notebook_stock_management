from tkinter import *
from tkinter import messagebox
import random,os,tempfile   

def bill():

    billnumber = random.randint(300,1000)

    def search_bill():
        for i in os.listdir("bills/"):
            if i.split(".")[0] == billnumberEntry.get():
                file = open(f'bills/{i}','r')
                textarea.delete(1.0,END)
                for j in file:
                    textarea.insert(End,j)
                file.close()
                break
        else:
            messagebox.showerror('Error',"INVALID BILL NUMBER!!!")
            
    def print_bill():
        if textarea.get(1.0,END) == "\n":
            messagebox.showerror("ERROR","BILL IS EMPTY!!!")
        else:
            file = tempfile.mktemp(".txt")
            open(file,"w").write(textarea.get(1.0,END))
            os.startfile(file,"print")

    if not os.path.exists("bills"):
        os.mkdir("bills")

    def clear():

        longsize1Entry.delete(0,END)
        longsize2Entry.delete(0,END)
        kingsize1Entry.delete(0,END)
        kingsize2Entry.delete(0,END)
        kingsize3Entry.delete(0,END)
        kingsize4Entry.delete(0,END)
        smallsize1Entry.delete(0,END)
        smallsize2Entry.delete(0,END)
        smallsize3Entry.delete(0,END)
        smallsize4Entry.delete(0,END)
        pendownbookEntry.delete(0,END)
        drawingbookEntry.delete(0,END)
        diaryEntry.delete(0,END)
        diary_sEntry.delete(0,END)
        journelEntry.delete(0,END)
        graphEntry.delete(0,END)
        practicalEntry.delete(0,END)
        pocket_diaryEntry.delete(0,END)

        longsize1Entry.insert(0,0)
        longsize2Entry.insert(0,0)
        kingsize1Entry.insert(0,0)
        kingsize2Entry.insert(0,0)
        kingsize3Entry.insert(0,0)
        kingsize4Entry.insert(0,0)
        smallsize1Entry.insert(0,0)
        smallsize2Entry.insert(0,0)
        smallsize3Entry.insert(0,0)
        smallsize4Entry.insert(0,0)
        pendownbookEntry.insert(0,0)
        drawingbookEntry.insert(0,0)
        diaryEntry.insert(0,0)
        diary_sEntry.insert(0,0)
        journelEntry.insert(0,0)
        graphEntry.insert(0,0)
        practicalEntry.insert(0,0)
        pocket_diaryEntry.insert(0,0)

        longsizepriceEntry.delete(0,END)
        kingsizepriceEntry.delete(0,END)
        smallsizepriceEntry.delete(0,END)
        pdpriceEntry.delete(0,END)
        ocpriceEntry.delete(0,END)
        taxEntry.delete(0,END)

        nameEntry.delete(0,END)
        phoneEntry.delete(0,END)
        billnoEntry.delete(0,END)
        addressEntry.delete(0,END)
        date_of_orderEntry.delete(0,END)
        date_of_deliveryEntry.delete(0,END)
        textarea.delete(1.0,END)
        
        
        

    def total():
        global LSnoteprice1,LSnoteprice2,KSnoteprice1,KSnoteprice2,KSnoteprice3,KSnoteprice4
        global SSnoteprice1,SSnoteprice2,SSnoteprice3,SSnoteprice4,PDbookprice,Dbookprice
        global Diaryprice,Diary_sprice ,Journelprice,Pocketdiaryprice,Practicalprice,Graphprice
        global totalbill

        LSnoteprice1 = int(longsize1Entry.get())*50
        LSnoteprice2= int(longsize2Entry.get())*50
        LSTotal = LSnoteprice1 + LSnoteprice2
        longsizepriceEntry.delete(0,END)
        longsizepriceEntry.insert(0,f'{LSTotal} Rs')

        KSnoteprice1= int(kingsize1Entry.get())*40
        KSnoteprice2 = int(kingsize2Entry.get())*40
        KSnoteprice3 = int(kingsize3Entry.get())*40
        KSnoteprice4 = int(kingsize4Entry.get())*40
        KSTotal = KSnoteprice1 + KSnoteprice2 +  KSnoteprice3 + KSnoteprice4
        kingsizepriceEntry.delete(0,END)
        kingsizepriceEntry.insert(0,str(KSTotal)+' Rs')

        SSnoteprice1= int(smallsize1Entry.get())*30
        SSnoteprice2= int(smallsize2Entry.get())*30
        SSnoteprice3= int(smallsize3Entry.get())*30
        SSnoteprice4= int(smallsize4Entry.get())*30
        SSTotal = SSnoteprice1 + SSnoteprice2 + SSnoteprice3 + SSnoteprice4
        smallsizepriceEntry.delete(0,END)
        smallsizepriceEntry.insert(0,str(SSTotal)+' Rs')

        PDbookprice = int(pendownbookEntry.get())*25
        Dbookprice = int(drawingbookEntry.get())*45
        PDTotal = PDbookprice + Dbookprice
        pdpriceEntry.delete(0,END)
        pdpriceEntry.insert(0,str(PDTotal)+' Rs')

        Diaryprice = int(diaryEntry.get())*80
        Diary_sprice = int(diary_sEntry.get())*120
        Journelprice = int(journelEntry.get())*100
        Pocketdiaryprice = int(pocket_diaryEntry.get())*35
        Practicalprice = int(practicalEntry.get())*90
        Graphprice = int(graphEntry.get())*25
        OCTotal = Diaryprice + Diary_sprice + Journelprice + Pocketdiaryprice +  Practicalprice + Graphprice
        ocpriceEntry.delete(0,END)
        ocpriceEntry.insert(0,str(OCTotal)+' Rs')
        Ttax=LSTotal+KSTotal+SSTotal+PDTotal+OCTotal
        totaltax = Ttax*0.12
        taxEntry.delete(0,END)
        taxEntry.insert(0,str(totaltax)+' Rs')

        totalbill =  LSTotal + KSTotal + SSTotal + PDTotal + OCTotal + totaltax

    billnumber = random.randint(300,1000)
    
    def save_bill():
        
        global billnumber
        result = messagebox.askyesno("Confirmation","DO YOU WANT TO SAVE THE BILL?")
        if result :
            bill_content = textarea.get(1.0,END)
            file = open(f'bills/ {billnumber}.txt','w')
            file.write(bill_content)
            file.close()
            messagebox.showinfo("SUCCESS",f"BILL NUMBER ({billnumber}) HAS BEEN SAVED SUCCESSFULLY!!!")
            
            
            
    def bill_area():
        if  nameEntry.get() == "" or phoneEntry.get() == "" or addressEntry.get() == '' or date_of_orderEntry.get() == '' or  date_of_deliveryEntry.get() == '':
            messagebox.showerror('Error','CUSTOMER DETAILS ARE REQUIRED !!!')
        elif longsizepriceEntry.get() == '' or kingsizepriceEntry.get() == '' or smallsizepriceEntry.get() == '' or pdpriceEntry.get() == '' or ocpriceEntry.get() == '' :
            messagebox.showerror('Error','NO PRODUCTS ARE SELECTED !!!')
        elif longsizepriceEntry.get() == '0 Rs' and kingsizepriceEntry.get() == '0 Rs' and smallsizepriceEntry.get() == '0 Rs' and pdpriceEntry.get() == '0 Rs' and ocpriceEntry.get() == '0 Rs' :
            messagebox.showerror('Error','NO PRODUCTS ARE SELECTED !!!')
        else:
            textarea.delete(1.0,END)
            textarea.insert(END,"\t\t** ! WELCOME CUSTOMER ! **\n")
            textarea.insert(END,f'\nBill Number : {billnumber}')
            textarea.insert(END,f'\nName of Enterprise : {nameEntry.get()}')
            textarea.insert(END,f'\nPhone Number : {phoneEntry.get()}')
            textarea.insert(END,f'\nAddress : {addressEntry.get()}')
            textarea.insert(END,f'\nDate of Order : {date_of_orderEntry.get()}')
            textarea.insert(END,f'\nDate of Delivery : {date_of_deliveryEntry.get()}')
            textarea.insert(END,f'\n=======================================================')
            textarea.insert(END,f'\nProduct\t\t\tQuantity\t\t\tPrice')
            textarea.insert(END,f'\n=======================================================')
            if  longsize1Entry.get() != '0':
                textarea.insert(END,f'Long size(unruled)\t\t\t{longsize1Entry.get()}\t\t\t{LSnoteprice1}  Rs')

            if longsize2Entry.get() != '0':
                textarea.insert(END,f'Long size(ruled)\t\t\t{longsize2Entry.get()}\t\t\t{LSnoteprice2}  Rs')

            if kingsize1Entry.get() != '0':
                textarea.insert(END,f'King size(unruled)\t\t\t{kingsize1Entry.get()}\t\t\t{KSnoteprice1}  Rs')

            if kingsize2Entry.get() != '0':
                textarea.insert(END,f'King size(ruled)\t\t\t{kingsize2Entry.get()}\t\t\t{KSnoteprice2}  Rs')

            if kingsize3Entry.get() != '0':
                textarea.insert(END,f'King size(two lines)\t\t\t{kingsize3Entry.get()}\t\t\t{KSnoteprice3}  Rs')

            if kingsize4Entry.get() != '0':
                textarea.insert(END,f'King size(four lines)\t\t\t{kingsize4Entry.get()}\t\t\t{KSnoteprice4}  Rs')

            if smallsize1Entry.get() != '0':
                textarea.insert(END,f'Small size(unruled)\t\t\t{smallsize1Entry.get()}\t\t\t{SSnoteprice1}  Rs')

            if smallsize2Entry.get() != '0':
                textarea.insert(END,f'Small size(ruled)\t\t\t{smallsize2Entry.get()}\t\t\t{SSnoteprice2}  Rs')

            if smallsize3Entry.get() != '0':
                textarea.insert(END,f'Small size(two lines)\t\t\t{smallsize3Entry.get()}\t\t\t{SSnoteprice3}  Rs')

            if smallsize4Entry.get() != '0':
                textarea.insert(END,f'Small size(four lines)\t\t\t{smallsize4Entry.get()}\t\t\t{SSnoteprice4}  Rs')

            if pendownbookEntry.get() != '0':
                textarea.insert(END,f'Pen down book\t\t\t{pendownbookEntry.get()}\t\t\t{PDbookprice}  Rs')

            if drawingbookEntry.get() != '0':
                textarea.insert(END,f'Drawing book\t\t\t{drawingbookEntry.get()}\t\t\t{Dbookprice}  Rs')

            if diaryEntry.get() != '0':
                textarea.insert(END,f'Diary\t\t\t{diaryEntry.get()}\t\t\t{Diaryprice}  Rs')
        
            if diary_sEntry.get() != '0':
                textarea.insert(END,f'Diary(Spiral)\t\t\t{diary_sEntry.get()}\t\t\t{Diary_sprice}  Rs')

            if journelEntry.get() != '0':
                textarea.insert(END,f'Journel\t\t\t{journelEntry.get()}\t\t\t{Journelprice}  Rs')

            if pocket_diaryEntry.get() != '0':
                textarea.insert(END,f'Pocket diary\t\t\t{pocket_diaryEntry.get()}\t\t\t{Pocketdiaryprice}  Rs')

            if practicalEntry.get() != '0':
                textarea.insert(END,f'Practical note\t\t\t{practicalEntry.get()}\t\t\t{Practicalprice}  Rs')

            if graphEntry.get() != '0':
                textarea.insert(END,f'Graph note\t\t\t{graphEntry.get()}\t\t\t{Graphprice}  Rs')

            textarea.insert(END,f'\n-------------------------------------------------------')

            if taxEntry.get() != '0.0 Rs':
                textarea.insert(END,f'Total tax\t\t\t\t\t {taxEntry.get()}')

            textarea.insert(END,f'\n\nTotal Bill \t\t\t\t\t {totalbill}')
            textarea.insert(END,f'\n-------------------------------------------------------')
            save_bill()


    root = Tk()
    root.title("NOTEBOOK STOCK MANAGEMENT")
    headingLabel = Label(root,text = "NOTEBOOK STOCK MANAGEMENT",font = ("algerian",30,"bold")
                                        ,bg = "grey20",fg = "misty rose",bd = 12,relief = GROOVE)
    headingLabel.pack(fill = X,pady = 5)
    customer_details_frame = LabelFrame(root,text = "CUSTOMER DETAILS",font = ("times new roman",15,"bold")
                                                                      ,bg = "grey20",fg = "misty rose",bd = 8 , relief = GROOVE,)
    customer_details_frame.pack(fill = X)

    nameLabel = Label(customer_details_frame, text = "Name of enterprise",font = ("times new roman",15,"bold")
                                     ,bg = "dark slate grey",fg = "white")
    nameLabel.grid(row = 0 , column = 0,padx = 20,pady = 2)

    nameEntry = Entry(customer_details_frame,font = ("georgia",15), bd = 7,width = 18)
    nameEntry.grid(row = 0 , column = 1,padx = 8)

    phoneLabel = Label(customer_details_frame, text = "Phone number",font = ("times new roman",15,"bold")
                                     ,bg = "dark slate grey",fg = "white")
    phoneLabel.grid(row = 0 , column = 2,padx = 20)

    phoneEntry = Entry(customer_details_frame,font =( "georgia",15), bd = 7,width = 18)
    phoneEntry.grid(row = 0 , column = 3,padx = 8)

    billnumberLabel = Label(customer_details_frame, text = "Bill number",font = ("times new roman",15,"bold")
                                     ,bg = "dark slate grey",fg = "white")
    billnumberLabel.grid(row = 0 , column = 4,padx = 20,pady = 2)

    billnoEntry = Entry(customer_details_frame,font = ("georgia",15), bd = 7,width = 18)
    billnoEntry.grid(row = 0 , column = 5,padx = 8)

    addressLabel = Label(customer_details_frame, text = "Address",font = ("times new roman",15,"bold")
                                     ,bg = "dark slate grey",fg = "white")
    addressLabel.grid(row = 1 , column = 0,padx = 20,pady = 2)

    addressEntry = Entry(customer_details_frame,font = ("georgia",15), bd = 7,width = 18)
    addressEntry.grid(row = 1 , column = 1, padx = 8)

    date_of_orderLabel = Label(customer_details_frame, text = "Date of order",font = ("times new roman",15,"bold")
                                     ,bg = "dark slate grey",fg = "white")
    date_of_orderLabel.grid(row = 1 , column =2 ,padx = 20,pady = 2)

    date_of_orderEntry = Entry(customer_details_frame,font = ("georgia",15), bd = 7,width = 18)
    date_of_orderEntry.grid(row = 1 , column = 3,padx = 8)

    date_of_deliveryLabel = Label(customer_details_frame, text = "Date of delivery",font = ("times new roman",15,"bold")
                                     ,bg = "dark slate grey",fg = "white")
    date_of_deliveryLabel.grid(row = 1 , column = 4,padx = 20,pady = 2)

    date_of_deliveryEntry = Entry(customer_details_frame,font = ("georgia",15), bd = 7,width = 18)
    date_of_deliveryEntry.grid(row = 1 , column = 5,padx = 8)

    searchButton = Button(customer_details_frame,text = "SEARCH",font = ("georgia",12 , "bold")
                          ,bd = 7,width = 16,command = search_bill)
    searchButton.grid(row = 0, column = 6, padx = 20, pady = 8)

    productsFrame = Frame(root)
    productsFrame.pack(pady = 5)

    notebooksFrame = LabelFrame(productsFrame, text = "Notebooks",font = ("times new roman",15,"bold")
                                ,bg = "grey20",fg = "misty rose",bd = 8 , relief = GROOVE,)
    notebooksFrame.grid(row = 0, column = 0)

    longsize1Label = Label(notebooksFrame , text = "Longsize(unruled)",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    longsize1Label.grid(row = 0, column = 0, pady = 9,padx = 10,sticky = "W")

    longsize1Entry = Entry(notebooksFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    longsize1Entry.grid(row = 0,column = 1, pady = 9,padx = 10)
    longsize1Entry.insert(0,0)

    longsize2Label = Label(notebooksFrame , text = "Longsize(single line)",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    longsize2Label.grid(row = 1, column = 0, pady = 9,padx = 10,sticky = "W")

    longsize2Entry = Entry(notebooksFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    longsize2Entry.grid(row = 1,column = 1, pady = 9,padx = 10)
    longsize2Entry.insert(0,0)

    kingsize1Label = Label(notebooksFrame , text = "Kingsize(unruled)",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    kingsize1Label.grid(row = 2, column = 0, pady = 9,padx = 10,sticky = "W")

    kingsize1Entry = Entry(notebooksFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    kingsize1Entry.grid(row = 2,column = 1, pady = 9,padx = 10)
    kingsize1Entry.insert(0,0)

    kingsize2Label = Label(notebooksFrame , text = "Kingsize(single line)",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    kingsize2Label.grid(row = 3, column = 0, pady = 9,padx = 10,sticky = "W")

    kingsize2Entry = Entry(notebooksFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    kingsize2Entry.grid(row = 3,column = 1, pady = 9,padx = 10)
    kingsize2Entry.insert(0,0)

    smallsize1Label = Label(notebooksFrame , text = "Smallsize(unruled)",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    smallsize1Label.grid(row = 4, column = 0, pady = 9,padx = 10,sticky = "W")

    smallsize1Entry = Entry(notebooksFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    smallsize1Entry.grid(row = 4,column = 1, pady = 9,padx = 10)
    smallsize1Entry.insert(0,0)

    smallsize2Label = Label(notebooksFrame , text = "Smallsize(single line)",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    smallsize2Label.grid(row = 5, column = 0, pady = 9,padx = 10,sticky = "W")

    smallsize2Entry = Entry(notebooksFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    smallsize2Entry.grid(row = 5,column = 1, pady = 9,padx = 10)
    smallsize2Entry.insert(0,0)

    notebooks_2_4Frame = LabelFrame(productsFrame, text = "Notebooks",font = ("times new roman",15,"bold")
                                ,bg = "grey20",fg = "misty rose",bd = 8 , relief = GROOVE,)
    notebooks_2_4Frame.grid(row = 0, column = 1)

    kingsize3Label = Label(notebooks_2_4Frame , text = "Kingsize(two lines)",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    kingsize3Label.grid(row = 0, column = 0, pady = 9,padx = 10,sticky = "W")

    kingsize3Entry = Entry(notebooks_2_4Frame ,font = ("times new roman",15),width = 10 , bd = 5)
    kingsize3Entry.grid(row = 0,column = 1, pady = 9,padx = 10)
    kingsize3Entry.insert(0,0)

    kingsize4Label = Label(notebooks_2_4Frame , text = "Kingsize(four lines)",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    kingsize4Label.grid(row = 1, column = 0, pady = 9,padx = 10,sticky = "W")

    kingsize4Entry = Entry(notebooks_2_4Frame ,font = ("times new roman",15),width = 10 , bd = 5)
    kingsize4Entry.grid(row = 1,column = 1, pady = 9,padx = 10)
    kingsize4Entry.insert(0,0)

    smallsize3Label = Label(notebooks_2_4Frame , text = "Smallsize(two lines)",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    smallsize3Label.grid(row = 2, column = 0, pady = 9,padx = 10,sticky = "W")

    smallsize3Entry = Entry(notebooks_2_4Frame ,font = ("times new roman",15),width = 10 , bd = 5)
    smallsize3Entry.grid(row = 2,column = 1, pady = 9,padx = 10)
    smallsize3Entry.insert(0,0)

    smallsize4Label = Label(notebooks_2_4Frame , text = "Smallsize(four lines)",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    smallsize4Label.grid(row = 3, column = 0, pady = 9,padx = 10,sticky = "W")

    smallsize4Entry = Entry(notebooks_2_4Frame ,font = ("times new roman",15),width = 10 , bd = 5)
    smallsize4Entry.grid(row = 3,column = 1, pady = 9,padx = 10)
    smallsize4Entry.insert(0,0)

    drawingbookLabel = Label(notebooks_2_4Frame , text = "Drawing Book",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    drawingbookLabel.grid(row = 4, column = 0, pady = 9,padx = 10,sticky = "W")

    drawingbookEntry = Entry(notebooks_2_4Frame ,font = ("times new roman",15),width = 10 , bd = 5)
    drawingbookEntry.grid(row = 4,column = 1, pady = 9,padx = 10)
    drawingbookEntry.insert(0,0)

    pendownbookLabel = Label(notebooks_2_4Frame , text = "Pendown Notebook",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    pendownbookLabel.grid(row = 5, column = 0, pady = 9,padx = 10,sticky = "W")

    pendownbookEntry = Entry(notebooks_2_4Frame ,font = ("times new roman",15),width = 10 , bd = 5)
    pendownbookEntry.grid(row = 5,column = 1, pady = 9,padx = 10)
    pendownbookEntry.insert(0,0)

    ocFrame = LabelFrame(productsFrame, text = "Other catagories",font = ("times new roman",15,"bold")
                                ,bg = "grey20",fg = "misty rose",bd = 8 , relief = GROOVE,)
    ocFrame.grid(row = 0, column = 2)

    diaryLabel = Label(ocFrame , text = "Diary",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    diaryLabel.grid(row = 0, column = 0, pady = 9,padx = 10,sticky = "W")

    diaryEntry = Entry(ocFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    diaryEntry.grid(row = 0,column = 1, pady = 9,padx = 10)
    diaryEntry.insert(0,0)

    diary_sLabel = Label(ocFrame , text = "Diary(spiral)",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    diary_sLabel.grid(row = 1, column = 0, pady = 9,padx = 10,sticky = "W")

    diary_sEntry = Entry(ocFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    diary_sEntry.grid(row = 1,column = 1, pady = 9,padx = 10)
    diary_sEntry.insert(0,0)

    journelLabel = Label(ocFrame , text = "Jounel(spiral)",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    journelLabel.grid(row = 2, column = 0, pady = 9,padx = 10,sticky = "W")

    journelEntry = Entry(ocFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    journelEntry.grid(row = 2,column = 1, pady = 9,padx = 10)
    journelEntry.insert(0,0)

    pocket_diaryLabel = Label(ocFrame , text = "Pocket Diary",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    pocket_diaryLabel.grid(row = 3, column = 0, pady = 9,padx = 10,sticky = "W")

    pocket_diaryEntry = Entry(ocFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    pocket_diaryEntry.grid(row = 3,column = 1, pady = 9,padx = 10)
    pocket_diaryEntry.insert(0,0)

    practicalLabel = Label(ocFrame , text = "Practical Notebook",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    practicalLabel.grid(row = 4, column = 0, pady = 9,padx = 10,sticky = "W")

    practicalEntry = Entry(ocFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    practicalEntry.grid(row = 4,column = 1, pady = 9,padx = 10)
    practicalEntry.insert(0,0)

    graphLabel = Label(ocFrame , text = "Graph Notebook",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    graphLabel.grid(row = 5, column = 0, pady = 9,padx = 10,sticky = "W")

    graphEntry = Entry(ocFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    graphEntry.grid(row = 5,column = 1, pady = 9,padx = 10)
    graphEntry.insert(0,0)

    billFrame = Frame(productsFrame, bd = 8, relief = GROOVE)
    billFrame.grid(row = 0, column = 3,padx = 10)

    billareaLabel = Label(billFrame,text = "Bill area",font = ("times new roman",15) , bd = 7, relief = GROOVE)
    billareaLabel.pack(fill = X)

    scrollbar = Scrollbar(billFrame ,orient = VERTICAL)
    scrollbar.pack(side = RIGHT ,fill = Y)  

    textarea  = Text (billFrame, height = 18,width = 55, yscrollcommand = scrollbar.set)
    textarea.pack()

    scrollbar.config(command = textarea.yview)

    billmenuFrame = LabelFrame(root, text = "Bill Menu",font = ("times new roman",15,"bold")
                                ,bg = "grey20",fg = "misty rose",bd = 8 , relief = GROOVE,)
    billmenuFrame.pack()

    longsizepriceLabel = Label(billmenuFrame , text = "LS note Price",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    longsizepriceLabel.grid(row = 0, column = 0, pady = 6,padx = 10,sticky = "W")

    longsizepriceEntry = Entry(billmenuFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    longsizepriceEntry.grid(row = 0,column = 1, pady = 6,padx = 10)

    kingsizepriceLabel = Label(billmenuFrame , text = "KS note Price",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    kingsizepriceLabel.grid(row = 1, column = 0, pady = 6,padx = 10,sticky = "W")

    kingsizepriceEntry = Entry(billmenuFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    kingsizepriceEntry.grid(row = 1,column = 1, pady = 6,padx = 10)

    smallsizepriceLabel = Label(billmenuFrame , text = "SS note Price",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    smallsizepriceLabel.grid(row = 2, column = 0, pady = 6,padx = 10,sticky = "W")

    smallsizepriceEntry = Entry(billmenuFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    smallsizepriceEntry.grid(row = 2,column = 1, pady = 6,padx = 10)

    ocpriceLabel = Label(billmenuFrame , text = "Other Catagories Price",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    ocpriceLabel.grid(row = 0, column = 2, pady = 6,padx = 10,sticky = "W")

    ocpriceEntry = Entry(billmenuFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    ocpriceEntry.grid(row = 0,column = 3, pady = 6,padx = 10)

    pdpriceLabel = Label(billmenuFrame , text = "Pendown_DrawNBPrice",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    pdpriceLabel.grid(row = 1, column = 2, pady = 6,padx = 10,sticky = "W")
    pdpriceEntry = Entry(billmenuFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    pdpriceEntry.grid(row = 1,column = 3, pady = 6,padx = 10)

    taxLabel = Label(billmenuFrame , text = " Notebook Tax",font = ("times new roman",15,"bold")
                          ,bg = "dark slate grey",fg = "white")
    taxLabel.grid(row = 2, column = 2, pady = 6,padx = 10,sticky = "W")

    taxEntry = Entry(billmenuFrame ,font = ("times new roman",15),width = 10 , bd = 5)
    taxEntry.grid(row = 2,column = 3, pady = 6,padx = 10)

    buttonFrame = Frame(billmenuFrame, bd =8, relief = GROOVE)
    buttonFrame.grid(row = 0 , column = 4, rowspan = 3)

    totalbutton = Button(buttonFrame , text = "TOTAL",font = ("cosmic sans",16,"bold")
                         ,bg = "dark slate grey",fg = "white",bd = 5 , width = 8, pady = 10, command = total)
    totalbutton.grid(row = 0, column = 0,pady = 20,padx = 5)

    billbutton = Button(buttonFrame , text = "BILL",font = ("cosmic sans",16,"bold")
                         ,bg = "dark slate grey",fg = "white",bd = 5 , width = 8, pady = 10,command = bill_area)
    billbutton.grid(row = 0, column = 1,pady = 20,padx = 5)

    printbutton = Button(buttonFrame , text = "PRINT",font = ("cosmic sans",16,"bold")
                         ,bg = "dark slate grey",fg = "white",bd = 5 , width = 8, pady = 10,command = print_bill)
    printbutton.grid(row = 0, column = 3,pady = 20,padx = 5)

    clearbutton = Button(buttonFrame , text = "CLEAR",font = ("cosmic sans",16,"bold")
                         ,bg = "dark slate grey",fg = "white",bd = 5 , width = 8, pady = 10,command = clear)
    clearbutton.grid(row = 0, column = 4,pady = 20,padx = 5)

    root.mainloop()

