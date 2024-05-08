import arcpy


class Parsel_Zebt:
    def __init__(self,base_data_path,azcad_data_base,output_data_path,checkbox_value,textBrowser,readme,head):
        super().__init__()
        self.pay_zebt_append(base_data_path,azcad_data_base,output_data_path,checkbox_value,textBrowser,readme,head)
        
    def pay_zebt_append(self,base_data_path,azcad_data_base,output_data_path,checkbox_value,textBrowser,readme,head):
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor_=textBrowser.textCursor()
        
        try:
            arcpy.management.AddField(azcad_data_base+"\PAY_TORPAQ","Parsel_id", 'TEXT')
            arcpy.management.Append(base_data_path+'\Pay_torpaqi', azcad_data_base+'\PAY_TORPAQ', 'NO_TEST')
            
            count_quarter = arcpy.GetCount_management(azcad_data_base+'\QUARTER')
            count_quarter1 = str(count_quarter)
            if count_quarter1 != "0":
                arcpy.analysis.SpatialJoin(azcad_data_base+'\PAY_TORPAQ',azcad_data_base+'\QUARTER',output_data_path+'\quarter_pay','JOIN_ONE_TO_ONE', 'KEEP_ALL','','WITHIN')
                arcpy.management.AlterField(output_data_path+'\quarter_pay', 'QUARTER_NAME',"ADDRESS","ADDRESS", 'TEXT')
                arcpy.management.AlterField(output_data_path+'\quarter_pay', 'Rn',"REGISTER_NO","REGISTER_NO", 'TEXT')
                
            if count_quarter1 == "0":
                arcpy.management.CopyFeatures(azcad_data_base+'\PAY_TORPAQ',output_data_path+'\quarter_pay')
                arcpy.management.AlterField(output_data_path+'\quarter_pay', 'Rn',"REGISTER_NO","REGISTER_NO", 'TEXT')
            
            count_property_ = arcpy.GetCount_management(azcad_data_base+'\PROPERTY_GROUP')
            
            arcpy.management.AddField(output_data_path+"\quarter_pay","FK_PROPERTY_TYPE", 'SHORT')
            arcpy.management.AddField(output_data_path+"\quarter_pay","FK_OWNERSHIP_TYPE", 'SHORT')
            arcpy.management.AddField(output_data_path+"\quarter_pay","FK_IS_LEGAL", 'SHORT')
            arcpy.management.AddField(output_data_path+"\quarter_pay","TOTAL_AREA", 'DOUBLE')
            
            arcpy.management.CalculateField(output_data_path+'\quarter_pay', 'FK_PROPERTY_TYPE',0, 'PYTHON3')
            arcpy.management.CalculateField(output_data_path+'\quarter_pay', 'FK_OWNERSHIP_TYPE',2, 'PYTHON3')
            arcpy.management.CalculateField(output_data_path+'\quarter_pay', 'FK_IS_LEGAL',1, 'PYTHON3')
            arcpy.management.CalculateField(output_data_path+'\quarter_pay', 'TOTAL_AREA','!I_Ha!', 'PYTHON3')
            
            arcpy.management.Append(output_data_path+'\quarter_pay', azcad_data_base+'\PROPERTY_GROUP', 'NO_TEST')

            
            
            count_property1 = str(count_property_)
            count_property2 = int(count_property1)
            with arcpy.da.UpdateCursor(azcad_data_base+"\PAY_TORPAQ", ["FK_PROPERTY_GROUP"]) as cursor:
                nomre = count_property2
                for row in cursor:
                    nomre += 1
                    row[0] = nomre
                    cursor.updateRow(row)
            
            
            ####################################################################################################################################
            
            
            arcpy.analysis.Intersect([output_data_path+"\PARCEL",base_data_path+'\Zebt'],output_data_path+"\Parcel_Zebt", 'ALL')
            arcpy.management.AddField(azcad_data_base+"\OCCUPATION","Fk_Parsel", 'TEXT')
            
            arcpy.management.Append(output_data_path+"\Parcel_Zebt", azcad_data_base+'\OCCUPATION', 'NO_TEST')
            
            
            
            
            arcpy.management.MakeFeatureLayer(azcad_data_base+"\OCCUPATION","occu1")
            arcpy.management.MakeFeatureLayer(azcad_data_base+"\PAY_TORPAQ","pay1")
            arcpy.management.AddJoin("occu1", 'Fk_Parsel', "pay1", 'Parsel_id', 'KEEP_ALL')
            arcpy.management.CalculateField("occu1", 'OCCUPATION.FK_PAY_TORPAQ','!PAY_TORPAQ.OBJECTID!')
            arcpy.management.RemoveJoin("occu1", "PAY_TORPAQ")
            
            arcpy.management.CalculateField("occu1", 'TOTAL_AREA','round(!SHAPE_Area!,0)')
            
            arcpy.management.DeleteField(azcad_data_base+"\OCCUPATION","Fk_Parsel")
            
            arcpy.management.DeleteField(azcad_data_base+"\PAY_TORPAQ","Parsel_id")
            
            ################### relation quarter zebt ##############################
            # arcpy.analysis.Intersect([azcad_data_base+'\OCCUPATION',base_data_path+'\QUARTER'],output_data_path+"\Quarter_Zebt_relation", 'ALL')
            # arcpy.management.MakeFeatureLayer(output_data_path+"\Quarter_Zebt_relation","Quarter_Zebt_relation_make")
            # arcpy.management.MakeFeatureLayer(azcad_data_base+"\OCCUPATION","Zebt_make88")
            # arcpy.management.AddJoin("Zebt_make88", 'OBJECTID', "Quarter_Zebt_relation_make", 'FID_OCCUPATION', 'KEEP_ALL')
            # arcpy.management.CalculateField("Zebt_make88", 'OCCUPATION.FK_QUARTER','!Quarter_Zebt_relation.FID_QUARTER!')
            # arcpy.management.RemoveJoin("Zebt_make88", "Quarter_Zebt_relation")
            
            ################### relation quarter zebt ##############################
            
            ####################################### Pay Quarter relation   ###################################################################
            arcpy.analysis.Intersect([azcad_data_base+"\PAY_TORPAQ",base_data_path+'\QUARTER'],output_data_path+"\Pay_Quarter", 'ALL')
            
            arcpy.management.MakeFeatureLayer(output_data_path+"\Pay_Quarter","p_q1")
            
            arcpy.management.MakeFeatureLayer(azcad_data_base+"\PAY_TORPAQ","p1")
            
            arcpy.management.AddJoin("p1", 'OBJECTID', "p_q1", 'FID_PAY_TORPAQ', 'KEEP_ALL')
            arcpy.management.CalculateField("p1", 'PAY_TORPAQ.FK_QUARTER','!Pay_Quarter.FID_QUARTER!')
            arcpy.management.RemoveJoin('P1', 'Pay_Quarter')
            
            
            ####################################### Pay Quarter relation   ###################################################################
            
            arcpy.analysis.Intersect([azcad_data_base+"\OCCUPATION",azcad_data_base+'\PARCEL'],output_data_path+"\Parcel_OCCUPATION", 'ALL')
            
            arcpy.management.MakeFeatureLayer(output_data_path+"\Parcel_OCCUPATION","p_o1")
            
            arcpy.management.MakeFeatureLayer(azcad_data_base+"\OCCUPATION","o1")
            
            arcpy.management.AddJoin("o1", 'OBJECTID', "p_o1", 'FID_OCCUPATION', 'KEEP_ALL')
            arcpy.management.CalculateField("o1", 'OCCUPATION.FK_PARCEL','!Parcel_OCCUPATION.FID_PARCEL!')
            
            arcpy.management.RemoveJoin('o1', 'Parcel_OCCUPATION')
            
            
            
            ###################################### occupation admin uni relation  #########################
            
            arcpy.analysis.Intersect([azcad_data_base+"\OCCUPATION",azcad_data_base+'\SECTOR'],output_data_path+"\Parcel_SECTOR", 'ALL')
            
            arcpy.management.MakeFeatureLayer(output_data_path+"\Parcel_SECTOR","p_s1")
            
            arcpy.management.MakeFeatureLayer(azcad_data_base+"\OCCUPATION","o55")
            
            arcpy.management.AddJoin("o55", 'OBJECTID', "p_s1", 'FID_OCCUPATION', 'KEEP_ALL')
            
            arcpy.management.CalculateField("o55", 'OCCUPATION.FK_ADMIN_UNIT','!Parcel_SECTOR.Temp!')
            
            arcpy.management.RemoveJoin('o55', 'Parcel_SECTOR')
            
            ###################################### occupation admin uni relation  #########################
            
            ###################################### Pay to certificate #####################################
            
            count_property_for_zebt = arcpy.GetCount_management(azcad_data_base+'\PROPERTY_GROUP')
            count_property_for_zebt1 = str(count_property_for_zebt)
            count_property_for_zebt2 = int(count_property_for_zebt1)
            count_property_for_zebt2 = count_property_for_zebt2+1
            
            arcpy.management.CopyFeatures(azcad_data_base+'\PAY_TORPAQ',output_data_path+'\Pay_To_Certificate')
            
            arcpy.MakeFeatureLayer_management(output_data_path+'\Pay_To_Certificate', "Pay_torpaqi_lyr")
            arcpy.AddField_management("Pay_torpaqi_lyr","FK_CERTIFICATION_TYPE","TEXT")
            arcpy.AddField_management("Pay_torpaqi_lyr","FK_ORGANIZATION","TEXT")
            

            expression = "Jn IS NULL OR Jn = ''" 
            arcpy.SelectLayerByAttribute_management("Pay_torpaqi_lyr", 'NEW_SELECTION', expression)
            arcpy.CalculateField_management("Pay_torpaqi_lyr", 'Jn', '!Rn!', 'PYTHON3', None)
            arcpy.management.AlterField('Pay_torpaqi_lyr', 'Jn','CERTIFICATION_NO')
            
            arcpy.management.Append("Pay_torpaqi_lyr", azcad_data_base+'\CERTIFICATE', 'NO_TEST')
            
            
            expression2 = 'FK_PROPERTY_GROUP IS NULL'
            fields = ['FK_PROPERTY_GROUP']
            with arcpy.da.UpdateCursor(azcad_data_base+'\CERTIFICATE', fields, where_clause=expression2) as cursor:
                for row in cursor:

                    row[0] = count_property_for_zebt2
                    start_value += 1
                    cursor.updateRow(row)
        
                    
            ###################################### Pay to certificate #####################################
            
            
            
            ###################################### Certificate ############################################
            
            expression3 = 'CHAR_LENGTH(CERTIFICATION_NO) <>12'
            fields = ['FK_CERTIFICATION_TYPE']
            with arcpy.da.UpdateCursor(azcad_data_base+'\CERTIFICATE', fields, where_clause=expression3) as cursor:
                for row in cursor:

                    row[0] = 14
                    cursor.updateRow(row)
                    
                
                    
                    
            fields = ['FK_ORGANIZATION']
            with arcpy.da.UpdateCursor(azcad_data_base+'\CERTIFICATE', fields, where_clause=expression3) as cursor:
                for row in cursor:

                    row[0] = 1
                    cursor.updateRow(row)
                    
                    
                    
            expression4 = 'CHAR_LENGTH(CERTIFICATION_NO) >5'
            fields = ['FK_CERTIFICATION_TYPE']
            with arcpy.da.UpdateCursor(azcad_data_base+'\CERTIFICATE', fields, where_clause=expression4) as cursor:
                for row in cursor:

                    row[0] = 12
                    cursor.updateRow(row)
                    
                    
            fields = ['FK_ORGANIZATION']
            with arcpy.da.UpdateCursor(azcad_data_base+'\CERTIFICATE', fields, where_clause=expression4) as cursor:
                for row in cursor:

                    row[0] = 0
                    cursor.updateRow(row)
                    
                    
            if checkbox_value:
                readme.write("\n")
                readme.write("\n33. Pay torpagi ve zebt ile bagli butun prosesler hell edildi")
            cursor_.insertHtml('''<p><span style="color:green;">Pay torpağı və zəbt ilə bağlı bütün proseslər həll edildi <br> </span>''')
            cursor_.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong><br> </span>''')
                    
                
            ###################################### Certificate ############################################
            
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n34. Pay torpagi ve zebt ile bagli proseslerde xeta bas verdi! Araliq bazada Pay ve Zebtin movcudlugundan ve standartligidan emin olun!")
            cursor_.insertHtml('''<p><span style="color:red;">Pay torpağı və zəbt ilə bağlı proseslərdə xəta baş verdi! Aralıq bazada
                              Pay və Zəbtin mövcudluğundan və standartlığından əmin olun! <br> </span>''')
            cursor_.insertHtml('''<p><span style="color:black;"> <strong>-----------------------------------------------------------------</strong> <br> </span>''')
        
        
        if checkbox_value:    
            readme.close()
        
        
        
        
        
        
        





