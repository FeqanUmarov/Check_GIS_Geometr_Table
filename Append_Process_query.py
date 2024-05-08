import arcpy
from arcpy import env


class Append:
    def __init__(self,output_data_path,azcad_data_base,checkbox_value,textBrowser,readme,head):
        super().__init__()
        self.append_process(output_data_path,azcad_data_base,checkbox_value,textBrowser,readme,head)

    
    def append_process(self,output_data_path,azcad_data_base,checkbox_value,textBrowser,readme,head):
        layer = ['PARCEL','PARCEL_Property','BUILDING','Building_Property','AUXILIARY_BUILDING','AUXILIARY_Property',
            'PARCEL_Certificate','Building_Certificate','PARCEL_Property_Owner','PARCEL_Owner',
            'Building_Property_Owner','Building_Owner','ZONE1','SECTOR','ADMIN_UNIT']
        env.workspace = output_data_path
        
        
        


        for data in layer:
            if data == 'PARCEL':
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                try:
                    arcpy.management.Append(output_data_path+'\PARCEL', azcad_data_base+'\PARCEL', 'NO_TEST')
                    arcpy.management.CalculateField(azcad_data_base+"\PARCEL", "FK_PROPERTY_GROUP" ,"!OBJECTID!", 'PYTHON3')
                    arcpy.management.CalculateField(azcad_data_base+"\PARCEL", "PARCEL_NO" ,"!OBJECTID!", 'PYTHON3')
                        
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n18. Parcel layi Azcad bazasina load edildi")
                    cursor_.insertHtml('''<p><span style="color:green;">Parcel layı Azcad bazasına load edildi. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong><br> </span>''')
                
                except:    
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n18. Parcel layi Azcad bazasina load edile bilmedi. Araliq bazada Torpaq tum layinin movcudlugunu ve standart olmasini yoxlayin!")
                    cursor_.insertHtml('''<p><span style="color:red;"> Parcel layı load edilə bilmədi. Aralıq bazada Torpaq tum layının
                                mövcudluğunu və standart olmasını yoxlayın! <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong><br> </span>''')
                    
                if checkbox_value:     
                    readme.close()
            
           
            if data == 'BUILDING':
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                try:
                    count_property = arcpy.GetCount_management(azcad_data_base+'\PROPERTY_GROUP')
                    count_property1 = str(count_property)
                    count_property2 = int(count_property1)
                    arcpy.management.Append(output_data_path+'\BUILDING', azcad_data_base+'\BUILDING', 'NO_TEST')
                    with arcpy.da.UpdateCursor(azcad_data_base+"\BUILDING", ["FK_PROPERTY_GROUP"]) as cursor:
                        nomre = count_property2
                        for row in cursor:
                            nomre += 1
                            row[0] = nomre
                            cursor.updateRow(row)

                    arcpy.analysis.Intersect([azcad_data_base+"\BUILDING",azcad_data_base+'\PARCEL'],output_data_path+"\inter", 'ALL')

                    arcpy.management.MakeFeatureLayer(azcad_data_base+"\BUILDING","make_buil77")
                    arcpy.management.MakeFeatureLayer(output_data_path+"\inter","make_inter77")
                    arcpy.management.AddJoin("make_buil77", 'OBJECTID', "make_inter77", 'FID_BUILDING', 'KEEP_ALL')
                    arcpy.management.CalculateField("make_buil77", 'BUILDING.FK_PARCEL','!inter.FID_PARCEL!')
                    arcpy.management.RemoveJoin("make_buil77", "inter")
                    
                        
                        
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n20. Building layi Azcad bazasina load edildi")
                 
                    
                    cursor_.insertHtml('''<p><span style="color:green;">Building layı Azcad bazasına load edildi. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong><br> </span>''')
                    
                except:
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n20. Building layi Azcad bazasina load edile bilmedi. Araliq bazada Tikili tum layinin movcudlugunu ve standart olmasini yoxlayin!")
                    cursor_.insertHtml('''<p><span style="color:red;"> Building layı load edilə bilmədi. Aralıq bazada Tikili tum layının mövcudluğunu və standart olmasını yoxlayın! <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                    
                    
                if checkbox_value:     
                    readme.close()
                

            
                
            if data == "PARCEL_Property":
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                try:
                    arcpy.management.Append(output_data_path+'\PARCEL_Property', azcad_data_base+'\PROPERTY_GROUP', 'NO_TEST')
                    
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n19. Property group cedveline Parcel melumatlari load edildi")
                    cursor_.insertHtml('''<p><span style="color:green;">Property group cədvəlinə Parcel məlumatları load edildi. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong><br> </span>''')
                    
                except:
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n19. Property group cedveline Parcel melumatlari load edilmedi! Neticeler ucun secilmis qovluqda PARCEL_Property layinin movcudlugunu yoxlayin")
                    cursor_.insertHtml('''<p><span style="color:red;"> Property group cədvəlinə Parcel məlumatları load edilmədi! Nəticələr üçün seçilmiş
                                        bazada PARCEL_Property layının mövcudluğunu yoxlayın. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                        
                        
                if checkbox_value:     
                    readme.close()
                
            if data == "Building_Property":
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                try:
                    arcpy.management.Append(output_data_path+'\Building_Property', azcad_data_base+'\PROPERTY_GROUP', 'NO_TEST')
                    
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n21. Property group cedveline Building melumatlari load edildi")
                    cursor_.insertHtml('''<p><span style="color:green;">Property group cədvəlinə Building məlumatları load edildi. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                    
                except:
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n21. Property group cedveline Building melumatlari load edilmedi! Neticeler ucun secilmis bazada Building_Property layinin movcudlugunu yoxlayin")
                    cursor_.insertHtml('''<p><span style="color:red;"> Property group cədvəlinə Building məlumatları load edilmədi! Nəticələr üçün seçilmiş
                                  qovluqda Building_Property layının mövcudluğunu yoxlayın <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                if checkbox_value: 
                    readme.close()
                
            
            if data == 'AUXILIARY_Property':
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                try:
                    arcpy.management.Append(output_data_path+'\AUXILIARY_Property', azcad_data_base+'\PROPERTY_GROUP', 'NO_TEST')
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n23. Property group cedveline AUXILIARY melumatlari load edildi")
                    cursor_.insertHtml('''<p><span style="color:green;">Property group cədvəlinə AUXILIARY məlumatları load edildi. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                    
                except:
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n23. Property group cedveline AUXILIARY melumatlari load edilmedi! Neticeler ucun secilmis qovluqda AUXILIARY_Property layinin movcudlugunu yoxlayin")
                    cursor_.insertHtml('''<p><span style="color:red;"> Property group cədvəlinə AUXILIARY məlumatları load edilmədi! Nəticələr üçün seçilmiş
                                  qovluqda AUXILIARY_Property layının mövcudluğunu yoxlayın. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                if checkbox_value: 
                    readme.close()

            if data == 'AUXILIARY_BUILDING':
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                try:
                    count_property = arcpy.GetCount_management(azcad_data_base+'\PROPERTY_GROUP')
                    count_property1 = str(count_property)
                    count_property2 = int(count_property1)
                    arcpy.management.Append(output_data_path+'\AUXILIARY_BUILDING', azcad_data_base+'\AUXILIARY_BUILDING', 'NO_TEST')
                    with arcpy.da.UpdateCursor(azcad_data_base+"\AUXILIARY_BUILDING", ["FK_PROPERTY_GROUP"]) as cursor:
                        nomre = count_property2
                        for row in cursor:
                            nomre += 1
                            row[0] = nomre
                            cursor.updateRow(row)

                    arcpy.analysis.Intersect([azcad_data_base+"\AUXILIARY_BUILDING",azcad_data_base+'\PARCEL'],output_data_path+"\inter2", 'ALL')

                    arcpy.management.MakeFeatureLayer(azcad_data_base+"\AUXILIARY_BUILDING","make_AUX77")
                    arcpy.management.MakeFeatureLayer(output_data_path+"\inter2","make_inter777")
                    arcpy.management.AddJoin("make_AUX77", 'OBJECTID', "make_inter777", 'FID_AUXILIARY_BUILDING', 'KEEP_ALL')
                    arcpy.management.CalculateField("make_AUX77", 'AUXILIARY_BUILDING.FK_PARCEL','!inter2.FID_PARCEL!')
                    arcpy.management.RemoveJoin("make_AUX77", "inter2")
                    
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n22. AUXILIARY layina Komekci tikilinin melumatlari load edildi")
                    cursor_.insertHtml('''<p><span style="color:green;">AUXILIARY layına Komekci melumatlari load edildi. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                    
                except:
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n22. AUXILIARY layina Komekci tikilinin melumatlari load edile bilmedi. Neticeler ucun secilmis bazada AUXILIARY_BUILDING layinin movcudlugunu yoxlayin!")
                    cursor_.insertHtml('''<p><span style="color:red;">nAUXILIARY layına Komekci tikilinin melumatlari load edile bilmedi. Neticələr
                                      üçün seçilmiş bazada AUXILIARY_BUILDING mövcud olmasını yoxlayın! <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                
                if checkbox_value: 
                    readme.close()


            if data == "PARCEL_Certificate":
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                try:
                    arcpy.management.Append(output_data_path+'\PARCEL_Certificate', azcad_data_base+'\CERTIFICATE', 'NO_TEST')
                    arcpy.management.CalculateField(azcad_data_base+'\CERTIFICATE', "FK_PROPERTY_GROUP" ,"!OBJECTID!", 'PYTHON3')
                    
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n24. Certificate cedveline Parcel melumatlari load edildi")
                    cursor_.insertHtml('''<p><span style="color:green;">Certificate cədvəlinə Parcel məlumatları load edildi. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                    
                    
                except:
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n24. Certificate cedveline Parcel melumatlari load edilmedi! Neticeler ucun secilmis qovluqda PARCEL_Certificate layinin movcudlugunu yoxlayin")
                    cursor_.insertHtml('''<p><span style="color:red;"> Certificate cədvəlinə Parcel məlumatları load edilmədi! Nəticələr üçün seçilmiş
                                  qovluqda PARCEL_Certificate layının mövcudluğunu yoxlayın. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                
                if checkbox_value: 
                    readme.close()

            if data == "Building_Certificate":
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                
                try:
                    arcpy.management.Append(output_data_path+'\Building_Certificate', azcad_data_base+'\CERTIFICATE', 'NO_TEST')
                    arcpy.management.CalculateField(azcad_data_base+'\CERTIFICATE', 'FK_PROPERTY_GROUP','!OBJECTID!')
                    
                    count_null_certificate = arcpy.management.SelectLayerByAttribute(azcad_data_base+'\CERTIFICATE', 'NEW_SELECTION',"CERTIFICATION_DATE IS NULL And CERTIFICATION_NO IS NULL And CERTIFICATION_NO IS NULL And FK_CERTIFICATION_TYPE IS NULL And FILE_PATH IS NULL And DURATON_OF_USE IS NULL", 'NON_INVERT')
                    
                    count_null_certificate_count = arcpy.GetCount_management(count_null_certificate)
                    
                    count_null_certificate_count = str(count_null_certificate_count)
                    
                    
                    if count_null_certificate_count!="0":
                        arcpy.management.DeleteRows(count_null_certificate)
                        
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n25. Certificate cedveline Building melumatlari load edildi")
                    cursor_.insertHtml('''<p><span style="color:green;">Certificate cədvəlinə Building məlumatları load edildi. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                        
                except:
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n25. Certificate cedveline Building melumatlari load edilmedi! Neticeler ucun secilmis qovluqda Building_Certificate layinin movcudlugunu yoxlayin")
                    cursor_.insertHtml('''<p><span style="color:red;"> Certificate cədvəlinə Building məlumatları load edilmədi! Nəticələr üçün seçilmiş
                                  qovluqda Building_Certificate layının mövcudluğunu yoxlayın. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                
                if checkbox_value: 
                    readme.close()
                        
            if data == "PARCEL_Property_Owner":
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                
                try:
                    arcpy.management.Append(output_data_path+'\PARCEL_Property_Owner', azcad_data_base+'\PROPERTY_OWNER', 'NO_TEST')
                    
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n26. Property owner cedveline Parcel melumatlari load edildi")
                    cursor_.insertHtml('''<p><span style="color:green;">Property owner cədvəlinə Parcel məlumatları load edildi. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                except:
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n26. Property owner cedveline Parcel melumatlari load edilmedi! Neticeler ucun secilmis qovluqda PARCEL_Property_Owner layinin movcudlugunu yoxlayin")
                    cursor_.insertHtml('''<p><span style="color:red;"> Property owner cədvəlinə Parcel məlumatları load edilmədi! Nəticələr üçün seçilmiş
                                  qovluqda PARCEL_Property_Owner layının mövcudluğunu yoxlayın. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                
                if checkbox_value: 
                    readme.close()
                
            if data == "PARCEL_Owner":
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                
                try:
                    arcpy.management.Append(output_data_path+'\PARCEL_Owner', azcad_data_base+'\OWNER', 'NO_TEST')
                    
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n27. Owner cedveline Parcel melumatlari load edildi")
                    cursor_.insertHtml('''<p><span style="color:green;">Owner cədvəlinə Parcel məlumatları load edildi <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                except:
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n27. Owner cedveline Parcel melumatlari load edilmedi! Neticeler ucun secilmis qovluqda PARCEL_Owner layinin movcudlugunu yoxlayin")
                    cursor_.insertHtml('''<p><span style="color:red;"> Owner cədvəlinə Parcel məlumatları load edilmədi! Nəticələr üçün seçilmiş
                                  qovluqda PARCEL_Owner layının mövcudluğunu yoxlayın. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                if checkbox_value: 
                    readme.close()
                
            if data == "Building_Property_Owner":
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                
                try:
                    arcpy.management.Append(output_data_path+'\Building_Property_Owner', azcad_data_base+'\PROPERTY_OWNER', 'NO_TEST')
                    arcpy.management.CalculateField(azcad_data_base+'\PROPERTY_OWNER', "FK_PROPERTY_GROUP" ,"!OBJECTID!", 'PYTHON3')
                    arcpy.management.CalculateField(azcad_data_base+'\PROPERTY_OWNER', "FK_OWNER" ,"!OBJECTID!", 'PYTHON3')
                    
                    
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n28. Property owner cedveline Building melumatlari load edildi")
                    cursor_.insertHtml('''<p><span style="color:green;">Property owner cədvəlinə Building məlumatları load edildi. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                except:
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n28. Property owner cedveline Building melumatlari load edilmedi! Neticeler ucun secilmis qovluqda Building_Property_Owner layinin movcudlugunu yoxlayin")
                    cursor_.insertHtml('''<p><span style="color:red;"> Property owner cədvəlinə Building məlumatları load edilmədi! Nəticələr üçün seçilmiş
                                  qovluqda Building_Property_Owner layının mövcudluğunu yoxlayın. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                
                if checkbox_value: 
                    readme.close()
                
            if data == "Building_Owner":
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                
                try:
                    arcpy.management.Append(output_data_path+'\Building_Owner', azcad_data_base+'\OWNER', 'NO_TEST')
                    count_null_Owner = arcpy.management.SelectLayerByAttribute(azcad_data_base+'\OWNER', 'NEW_SELECTION',"FULL_NAME IS NULL And DATE_OF_BIRTH IS NULL And ID_CARD_NUMBER IS NULL")
                    count_null_Owner_count = arcpy.GetCount_management(count_null_Owner)
                    
                    count_null_Owner_count = str(count_null_Owner_count)
                    
                    
                    if count_null_Owner_count!="0":
                        arcpy.management.DeleteRows(count_null_Owner)
                        
                        
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n29. Owner cedveline Building melumatlari load edildi")
                    cursor_.insertHtml('''<p><span style="color:green;">Owner cədvəlinə Building məlumatları load edildi. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                        
                except:
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n29. Owner cedveline Building melumatlari load edilmedi! Neticeler ucun secilmis qovluqda Building_Owner layinin movcudlugunu yoxlayin")
                    cursor_.insertHtml('''<p><span style="color:red;"> Owner cədvəlinə Building məlumatları load edilmədi! Nəticələr üçün seçilmiş
                                  qovluqda Building_Owner layının mövcudluğunu yoxlayın. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                if checkbox_value: 
                    readme.close()


            if data == "ZONE1":
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                
                try:
                    arcpy.management.Append(output_data_path+'\ZONE1', azcad_data_base+'\ZONE1', 'NO_TEST')
                    arcpy.management.CalculateField(azcad_data_base+'\ZONE1', "TOTAL_AREA" ,"!SHAPE_Area!", 'PYTHON3')
                    arcpy.management.CalculateField(azcad_data_base+'\ZONE1', "FK_REGION" ,1, 'PYTHON3')
                    
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n30. Zone1 layina Zone1 melumatlari load edildi")
                    cursor_.insertHtml('''<p><span style="color:green;">Zone1 layına Zone1 məlumatları load edildi. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                    
                except:
                    if checkbox_value:
                        readme.write("\n30. Zone1 layina Zone1 melumatlari load edile bilmedi. Neticeler ucun secilmis bazada ZONE1 layinin movcudlugunu yoxlayin!")
                    cursor_.insertHtml('''<p><span style="color:red;">Zone1 layına Zone1 məlumatları load edilə bilmədi. Neticələr
                                      üçün seçilmiş bazada ZONE1 mövcud olmasını yoxlayın!. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                if checkbox_value: 
                    readme.close()

            if data == "SECTOR":
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                try:
                    arcpy.management.Append(output_data_path+'\SECTOR', azcad_data_base+'\SECTOR', 'NO_TEST')
                    arcpy.management.CalculateField(azcad_data_base+'\SECTOR', "FK_ZONE" ,1, 'PYTHON3')
                    
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n31. Sector layina Sector melumatlari load edildi")
                    cursor_.insertHtml('''<p><span style="color:green;">Sector layına Sector məlumatları load edildi. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                    
                except:
                    if checkbox_value:
                        readme.write("\n31.Sector layina Sector melumatlari load edile bilmedi. Neticeler ucun secilmis bazada SECTOR layinin movcudlugunu yoxlayin!")
                    cursor_.insertHtml('''<p><span style="color:red;">Sector layına Sector məlumatları load edilə bilmədi. Neticələr
                                      üçün seçilmiş bazada SECTOR mövcud olmasını yoxlayın! <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                if checkbox_value: 
                    readme.close()


            if data == "ADMIN_UNIT":
                if checkbox_value:
                    readme = open(head+"\\Readme.txt","a+")
                cursor_=textBrowser.textCursor()
                
                try:

                    arcpy.management.CopyFeatures(output_data_path+"\ZONE1",output_data_path+"\ZONE1_Admin")
                    arcpy.management.AddField(output_data_path+"\ZONE1_Admin","ADMIN_UNIT_CODE", 'TEXT')
                    arcpy.management.AddField(output_data_path+"\ZONE1_Admin","ADMIN_UNIT_NAME", 'TEXT')
                    arcpy.management.AddField(output_data_path+"\ZONE1_Admin","FK_PARENT", 'LONG')
                    arcpy.management.AddField(output_data_path+"\ZONE1_Admin","FK_ADMIN_LEVEL", 'SHORT')
                    arcpy.management.CalculateField(output_data_path+"\ZONE1_Admin", "ADMIN_UNIT_CODE" ,"!ZONE_CODE!", 'PYTHON3')
                    arcpy.management.CalculateField(output_data_path+"\ZONE1_Admin", "ADMIN_UNIT_NAME" ,"!ZONE_NAME!", 'PYTHON3')
                    arcpy.management.CalculateField(output_data_path+"\ZONE1_Admin", "FK_PARENT" ,1, 'PYTHON3')
                    arcpy.management.CalculateField(output_data_path+"\ZONE1_Admin", "FK_ADMIN_LEVEL" ,1, 'PYTHON3')
                    
                    arcpy.management.Append(output_data_path+'\ZONE1_Admin', azcad_data_base+'\ADMIN_UNIT', 'NO_TEST')

                    arcpy.management.CopyFeatures(output_data_path+"\SECTOR",output_data_path+"\SECTOR_Admin")
                    arcpy.management.AddField(output_data_path+"\SECTOR_Admin","ADMIN_UNIT_CODE", 'TEXT')
                    arcpy.management.AddField(output_data_path+"\SECTOR_Admin","ADMIN_UNIT_NAME", 'TEXT')
                    arcpy.management.AddField(output_data_path+"\SECTOR_Admin","FK_PARENT", 'LONG')
                    arcpy.management.AddField(output_data_path+"\SECTOR_Admin","FK_ADMIN_LEVEL", 'SHORT')
                    arcpy.management.CalculateField(output_data_path+"\SECTOR_Admin", "ADMIN_UNIT_CODE" ,"!SECTOR_CODE!", 'PYTHON3')
                    arcpy.management.CalculateField(output_data_path+"\SECTOR_Admin", "ADMIN_UNIT_NAME" ,"!SECTOR_NAME!", 'PYTHON3')
                    arcpy.management.CalculateField(output_data_path+"\SECTOR_Admin", "FK_PARENT" ,2, 'PYTHON3')
                    arcpy.management.CalculateField(output_data_path+"\SECTOR_Admin", "FK_ADMIN_LEVEL" ,2, 'PYTHON3')
                    arcpy.management.Append(output_data_path+'\SECTOR_Admin', azcad_data_base+'\ADMIN_UNIT', 'NO_TEST')

                    ############## relation with parcel ########################

                    arcpy.management.AddField(azcad_data_base+"\SECTOR","Temp", 'TEXT')

                    with arcpy.da.UpdateCursor(azcad_data_base+"\SECTOR", ["Temp"]) as cursor:
                        nomre = 2
                        for row in cursor:
                            nomre += 1
                            row[0] = nomre
                            cursor.updateRow(row)

                    arcpy.analysis.SpatialJoin(azcad_data_base+"\PARCEL", azcad_data_base+'\SECTOR',output_data_path+"\join_p_s", 'JOIN_ONE_TO_ONE', 'KEEP_ALL','', 'WITHIN')
                    arcpy.management.MakeFeatureLayer(azcad_data_base+"\PARCEL","make_parcel22")
                    arcpy.management.MakeFeatureLayer(output_data_path+"\join_p_s","make_spatial22")
                    arcpy.management.AddJoin("make_parcel22", 'OBJECTID', "make_spatial22", 'TARGET_FID', 'KEEP_ALL')
                    arcpy.management.CalculateField("make_parcel22", 'PARCEL.FK_ADMIN_UNIT','!join_p_s.Temp!')
                    arcpy.management.RemoveJoin("make_parcel22", "join_p_s")
                    arcpy.management.DeleteField("make_parcel22","Temp")
                    
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n32. Admin_Unit cedveline Sector melumatlari load edildi")
                    cursor_.insertHtml('''<p><span style="color:green;">Admin_Unit cədvəlinə Sector məlumatları load edildi. <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                    
                    
                except:
                    if checkbox_value:
                        readme.write("\n")
                        readme.write("\n32. Admin_Unit cedveline Sector melumatlari load edile bilmedi. Neticeler ucun secilmis bazada ADMIN_UNIT layinin movcudlugunu yoxlayin!")
                    cursor_.insertHtml('''<p><span style="color:red;">Admin_Unit cədvəlinə Sector məlumatları load edilə bilmədi. Neticələr
                                      üçün seçilmiş bazada Admin_Unit mövcud olmasını yoxlayın! <br> </span>''')
                    cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong> <br> </span>''')
                
                
                if checkbox_value: 
                    readme.close()
                
                
                ############## relation with parcel ########################

        
        

        
        
        
        
        
    
  
