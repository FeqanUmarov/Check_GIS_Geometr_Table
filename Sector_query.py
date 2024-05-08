import arcpy
from arcpy import env


class Sector:
    def __init__(self,base_data_path,output_data_path,checkbox_value,textBrowser,readme,head):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'
        self.write_sector(base_data_path,output_data_path,checkbox_value,textBrowser,readme,head)
        
        
    def write_sector(self,base_data_path,output_data_path,checkbox_value,textBrowser,readme,head):
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        
        try:
        
            arcpy.management.CopyFeatures(base_data_path+"\SECTOR",output_data_path+"\SECTOR")

            arcpy.management.CalculateField(output_data_path+"\SECTOR", "TOTAL_AREA" ,"!SHAPE_Area!", 'PYTHON3')
            if checkbox_value:
                readme.write("\n")
                readme.write("\n16. SECTOR layi export edildi")
            cursor.insertHtml('''<p><span style="color:green;">SECTOR layı export edildi <br> </span>''')
            cursor.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong><br> </span>''')
            
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n16. SECTOR layinin araliq bazada movcud olduguna diqqet edin!")
            cursor.insertHtml('''<p><span style="color:red;"SECTOR layının aralıq bazada mövcud olub olmadığına diqqət edin!<br> </span>''')
            cursor.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong><br> </span>''')
        if checkbox_value:     
            readme.close()



