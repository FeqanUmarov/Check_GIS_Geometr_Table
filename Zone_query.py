import arcpy
from arcpy import env


class Zone:
    def __init__(self,base_data_path,output_data_path,checkbox_value,textBrowser,readme,head):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'
        self.write_zone(base_data_path,output_data_path,checkbox_value,textBrowser,readme,head)
        
    def write_zone(self,base_data_path,output_data_path,checkbox_value,textBrowser,readme,head):
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        
        try:
            arcpy.management.CopyFeatures(base_data_path+"\Rayon_Serhed",output_data_path+"\ZONE1")
            if checkbox_value:
                readme.write("\n")
                readme.write("\n17. Zone layi export edildi")
            cursor.insertHtml('''<p><span style="color:green;">Zone layı export edildi <br> </span>''')
            cursor.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong><br> </span>''')
            
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n17. Zone layi export edile bilmedi. Araliq bazada Rayon_Serhed layinin movcudlugunu yoxlayin")
            cursor.insertHtml('''<p><span style="color:red;>"Zone layı export edilə bilmədi. Aralıq bazada Rayon_Serhed
                              layının mövcudluğunu yoxlayın! <br> </span>''')
            cursor.insertHtml('''<p><span style="color:black;"> <strong>-----------------------------------------------------------------</strong> <br> </span>''')
            
        if checkbox_value:     
            readme.close()




