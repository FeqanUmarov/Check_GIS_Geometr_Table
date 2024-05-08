import arcpy
from arcpy import env

class Ground_Control:
    def __init__(self,base_data_path,output_data_path,azcad_data_base,checkbox_value,textBrowser,readme,head):
        super().__init__()
        base_data_path = base_data_path +'\RAYON'
        self.write_GCP(base_data_path,output_data_path,azcad_data_base,checkbox_value,textBrowser,readme,head)
        
        
    def write_GCP(self,base_data_path,output_data_path,azcad_data_base,checkbox_value,textBrowser,readme,head):
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        
        try:
        
            env.workspace = base_data_path
            fcList = arcpy.ListFeatureClasses()

            if "Noqteler" in fcList:
                arcpy.management.CopyFeatures(base_data_path+r"\Noqteler",output_data_path+"\GROUND_CONTROL_POINT")
                arcpy.management.AddField(output_data_path+"\GROUND_CONTROL_POINT","POINT_X", 'DOUBLE')
                arcpy.management.AddField(output_data_path+"\GROUND_CONTROL_POINT","POINT_Y", 'DOUBLE')
                arcpy.management.CalculateField(output_data_path+"\GROUND_CONTROL_POINT","POINT_X","!X!", 'PYTHON3')
                arcpy.management.CalculateField(output_data_path+"\GROUND_CONTROL_POINT","POINT_Y","!Y!", 'PYTHON3')

            if "GPS" in fcList:
                arcpy.management.CopyFeatures(base_data_path+"\GPS",output_data_path+"\GROUND_CONTROL_POINT")
                arcpy.management.AddField(output_data_path+"\GROUND_CONTROL_POINT","POINT_X", 'DOUBLE')
                arcpy.management.AddField(output_data_path+"\GROUND_CONTROL_POINT","POINT_Y", 'DOUBLE')
                arcpy.management.CalculateField(output_data_path+"\GROUND_CONTROL_POINT","POINT_X","!X!", 'PYTHON3')
                arcpy.management.CalculateField(output_data_path+"\GROUND_CONTROL_POINT","POINT_Y","!Y!", 'PYTHON3')
                
                
            arcpy.management.Append(output_data_path+'\GROUND_CONTROL_POINT', azcad_data_base+'\GROUND_CONTROL_POINT', 'NO_TEST')
            
            if checkbox_value:
                readme.write("\n")
                readme.write("\n16. GPS layinda yeni sutunlar yaradildi ve kohne sutunlarda olan melumatlar kocuruldu")
            cursor.insertHtml('''<p><span style="color:green;">GPS layında yeni sütunlar yaradıldı və köhnə sütunlarda olan məlumatlar
                                  köçürüldü. <br> </span>''')
            cursor.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong><br> </span>''')
            
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n16. GPS layinda xeta yarandi. Araliq bazada GPS layinin movcudlugunu yoxlayin. Eger lay movcuddursa sutun adlarinin standart olmasina diqqet edin!")
            cursor.insertHtml('''<p><span style="color:red;">GPS layında xəta yarandı. Aralıq bazada GPS layının mövcudluğunu
                              yoxlayın. Əgər lay mövcuddursa sütun adlarının standart olmasına baxın!<br> </span>''')
            cursor.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong><br> </span>''')

        if checkbox_value:
            readme.close()