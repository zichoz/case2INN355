import pandas as pd
import datetime
import json

listWithCasesPrepared = []
event_conceptname = []
unique_eventuserids =  []
def load_data_pandas(filename):
    DataFrame = pd.read_csv(filename)   #Creates a dataframe of the data read by the read_csv()
    return DataFrame

def unique_in_list(list):
    uniqueList = []
    for x in list:
        if x not in uniqueList:
            uniqueList.append(x)
            #print("er ikke i")
    return uniqueList


def makeVariables(dict):
    olddict = dict
    #print(olddict)
    #json.dump(dict, file(r'C:\Users\Nicholas\Google Drive\A NMBU år 1\INF120\Case 2 inn355temp\outputdict.txt', 'w'))
    fh = open('casesUsers.txt', 'w')
    fx = open('casesLists.txt', 'w')
    fxx = open('casesIfStatements.txt', 'w')
    fxxx = open('casesForDataFrame.txt', 'w')
    for xsssss in dict:
        print(dict[xsssss])
    #print(dict.header())
    for cases in dict: # for loop for making all the different user/activity lists. This double for loop just creates a text file with code, which i have inserted
        for users in dict[cases]:
            #print(users)
            users[19] = users[19].replace(" ", "_")
            users[19] = users[19].replace(":", "")
            users[19] = users[19].replace("(", "")
            users[19] = users[19].replace(")", "")
            users[19] = users[19].replace(".", "")
            if users[19] not in event_conceptname:
                event_conceptname.append(users[19])
                fh.write("len("+(users[19]) + ")" + ", ")
                fx.write((users[19]) + " = [] \n")
                fxx.write("if c[19] == " + "'" + (users[19]) + "'" + ":\n \t" + (users[19])+".append(c[19]) \n")
                fxxx.write("' " + users[19] + "', ")


    print("len(%")
    for x in olddict: # for looping through the dict
        #print(olddict[x])
        new_variables(olddict[x])

def new_variables(case):
    #print("looper gjennom case")
    #print(case)
    throughtime = 0
    time_max = 0
    time_min = 100000000000000000000000000000
    #print(len(case))
    count_events = len(case)
    count_activities = []
    count_users = []
    count_ordervalue = 0
    count_processstart = []
    count_processend = []
    #list for activities
    Vendor_creates_debit_memo = []
    Create_Purchase_Order_Item = []
    Vendor_creates_invoice = []
    Record_Service_Entry_Sheet = []
    Record_Goods_Receipt = []
    Record_Invoice_Receipt = []
    Clear_Invoice = []
    Cancel_Invoice_Receipt = []
    Remove_Payment_Block = []
    SRM_Created = []
    SRM_Change_was_Transmitted = []
    SRM_Complete = []
    SRM_Awaiting_Approval = []
    SRM_Document_Completed = []
    SRM_In_Transfer_to_Execution_Syst = []
    SRM_Ordered = []
    Change_Price = []
    SRM_Deleted = []
    Cancel_Goods_Receipt = []
    SRM_Transfer_Failed_ESys = []
    Set_Payment_Block = []
    Change_Quantity = []
    Change_Delivery_Indicator = []
    Change_Approval_for_Purchase_Order = []
    Delete_Purchase_Order_Item = []
    Cancel_Subsequent_Invoice = []
    Create_Purchase_Requisition_Item = []
    Receive_Order_Confirmation = []
    Record_Subsequent_Invoice = []
    SRM_Transaction_Completed = []
    Change_Final_Invoice_Indicator = []
    SRM_Held = []
    SRM_Incomplete = []
    Reactivate_Purchase_Order_Item = []
    Change_Rejection_Indicator = []
    Change_Storage_Location = []
    Release_Purchase_Order = []
    Change_payment_term = []

    #lists to count how many times a user has touched the case
    NONE = []
    user_116 = []
    user_145 = []
    batch_00 = []
    user_024 = []
    user_008 = []
    user_007 = []
    user_015 = []
    user_004 = []
    user_001 = []
    user_006 = []
    user_013 = []
    user_019 = []
    user_002 = []
    user_020 = []
    user_012 = []
    batch_02 = []
    user_000 = []
    user_005 = []
    user_003 = []
    user_063 = []
    user_177 = []
    user_197 = []
    user_038 = []
    user_029 = []
    user_266 = []
    user_267 = []
    user_073 = []
    user_011 = []
    user_014 = []
    user_016 = []
    user_027 = []
    user_010 = []
    user_091 = []
    user_206 = []
    user_098 = []
    user_092 = []
    user_110 = []
    user_018 = []
    user_111 = []
    user_112 = []
    user_160 = []
    user_161 = []
    user_140 = []
    user_023 = []
    user_083 = []
    user_201 = []
    user_203 = []
    user_235 = []
    user_084 = []
    user_131 = []
    user_132 = []
    user_156 = []
    user_200 = []
    user_147 = []
    user_130 = []
    user_223 = []
    user_273 = []
    user_165 = []
    user_166 = []
    user_059 = []
    user_060 = []
    user_033 = []
    user_035 = []
    user_036 = []
    user_045 = []
    user_046 = []
    user_072 = []
    batch_06 = []
    user_079 = []
    user_080 = []
    user_032 = []
    user_031 = []
    user_117 = []
    user_054 = []
    user_118 = []
    user_138 = []
    batch_01 = []
    user_141 = []
    user_044 = []
    user_043 = []
    user_113 = []
    batch_10 = []
    user_154 = []
    user_172 = []
    batch_12 = []
    user_173 = []
    user_142 = []
    user_100 = []
    user_186 = []
    user_191 = []
    user_039 = []
    user_188 = []
    user_205 = []
    batch_07 = []
    user_070 = []
    user_202 = []
    user_124 = []
    user_009 = []
    user_017 = []
    user_040 = []
    user_164 = []
    user_216 = []
    user_192 = []
    user_198 = []
    user_208 = []
    user_222 = []
    user_144 = []
    user_228 = []
    user_094 = []
    batch_08 = []
    user_042 = []
    user_047 = []
    user_068 = []
    user_207 = []
    user_146 = []
    user_249 = []
    user_021 = []
    user_218 = []
    user_034 = []
    user_122 = []
    user_064 = []
    user_022 = []
    user_050 = []
    user_061 = []
    user_196 = []
    user_025 = []
    user_037 = []
    user_278 = []
    user_279 = []
    user_158 = []
    user_126 = []
    user_250 = []
    user_081 = []
    user_026 = []
    user_286 = []
    user_287 = []
    user_151 = []
    user_288 = []
    user_289 = []
    user_290 = []
    user_214 = []
    user_291 = []
    user_058 = []
    user_049 = []
    user_204 = []
    user_190 = []
    user_271 = []
    user_171 = []
    user_087 = []
    user_303 = []
    user_304 = []
    user_194 = []
    user_102 = []
    user_086 = []
    user_251 = []
    user_048 = []
    user_066 = []
    user_088 = []
    user_152 = []
    user_163 = []
    user_077 = []
    user_071 = []
    user_119 = []
    user_028 = []
    user_187 = []
    user_099 = []
    user_325 = []
    user_294 = []
    user_336 = []
    user_337 = []
    user_180 = []
    batch_13 = []
    user_057 = []
    user_169 = []
    user_211 = []
    user_125 = []
    user_262 = []
    user_339 = []
    user_308 = []
    user_362 = []
    user_340 = []
    user_365 = []
    user_105 = []
    user_299 = []
    user_306 = []
    user_115 = []
    user_127 = []
    user_272 = []
    user_256 = []
    user_396 = []
    user_136 = []
    user_178 = []
    user_121 = []
    batch_11 = []
    user_380 = []
    user_382 = []
    user_364 = []
    user_353 = []
    user_360 = []
    user_243 = []
    user_385 = []
    user_322 = []
    user_264 = []
    user_387 = []
    user_078 = []
    user_341 = []
    user_137 = []
    user_417 = []
    user_101 = []
    user_082 = []
    user_402 = []
    user_300 = []
    user_258 = []
    user_335 = []
    user_332 = []
    user_397 = []
    user_372 = []
    user_333 = []
    batch_15 = []
    user_427 = []
    user_075 = []
    user_238 = []
    user_451 = []
    user_453 = []
    user_486 = []
    user_480 = []
    user_421 = []
    user_374 = []
    batch_16 = []
    user_320 = []
    user_500 = []
    user_319 = []
    user_440 = []
    user_439 = []
    user_524 = []
    user_538 = []
    user_373 = []
    batch_17 = []
    user_549 = []
    user_464 = []
    user_123 = []
    user_392 = []
    user_424 = []
    user_212 = []
    user_461 = []
    user_481 = []
    user_220 = []
    user_556 = []
    user_093 = []
    user_470 = []
    user_085 = []
    user_444 = []
    user_590 = []
    user_363 = []
    user_381 = []
    user_305 = []
    user_224 = []
    batch_18 = []
    user_309 = []
    user_358 = []
    user_601 = []

    #end of lists with users

    case_name = 0
    case_spendareatext = 0
    case_company = 0
    case_document_type = 0
    case_sub_spend = 0
    case_purch_doc = 0
    case_vendor = 0
    case_item_type = 0
    case_item_category = 0
    case_spend_class = 0
    case_source = 0
    case_name_first = 0
    case_GR = 0
    case_item = 0
    case_goods_recieved = 0

    for c in case:
        timechecker = datetime.datetime.strptime(c[21],'%d-%m-%Y %H:%M:%S.%f') #converting the string to a datettime object
        timechecker = datetime.datetime.timestamp(timechecker)# converting to seconds
        count_ordervalue = c[20]
        case_name = c[15]
        case_spendareatext = c[1] #r
        case_company = c[2] # r
        case_document_type = c[3] # r
        case_sub_spend = c[4] #r
        case_purch_doc = c[5] # r? her er en feil
        case_vendor = c[7]
        case_item_type = c[8] #riktig
        case_item_category = c[9]
        case_spend_class = c[10]
        case_source = c[11]
        case_name_first = c[12]
        case_GR = c[13]
        case_item = c[14]
        case_goods_recieved= c[14]
        if c[19] == 'Vendor_creates_debit_memo':
            Vendor_creates_debit_memo.append(c[19])
        if c[19] == 'Create_Purchase_Order_Item':
            Create_Purchase_Order_Item.append(c[19])
        if c[19] == 'Vendor_creates_invoice':
            Vendor_creates_invoice.append(c[19])
        if c[19] == 'Record_Service_Entry_Sheet':
            Record_Service_Entry_Sheet.append(c[19])
        if c[19] == 'Record_Goods_Receipt':
            Record_Goods_Receipt.append(c[19])
        if c[19] == 'Record_Invoice_Receipt':
            Record_Invoice_Receipt.append(c[19])
        if c[19] == 'Clear_Invoice':
            Clear_Invoice.append(c[19])
        if c[19] == 'Cancel_Invoice_Receipt':
            Cancel_Invoice_Receipt.append(c[19])
        if c[19] == 'Remove_Payment_Block':
            Remove_Payment_Block.append(c[19])
        if c[19] == 'SRM_Created':
            SRM_Created.append(c[19])
        if c[19] == 'SRM_Change_was_Transmitted':
            SRM_Change_was_Transmitted.append(c[19])
        if c[19] == 'SRM_Complete':
            SRM_Complete.append(c[19])
        if c[19] == 'SRM_Awaiting_Approval':
            SRM_Awaiting_Approval.append(c[19])
        if c[19] == 'SRM_Document_Completed':
            SRM_Document_Completed.append(c[19])
        if c[19] == 'SRM_In_Transfer_to_Execution_Syst':
            SRM_In_Transfer_to_Execution_Syst.append(c[19])
        if c[19] == 'SRM_Ordered':
            SRM_Ordered.append(c[19])
        if c[19] == 'Change_Price':
            Change_Price.append(c[19])
        if c[19] == 'SRM_Deleted':
            SRM_Deleted.append(c[19])
        if c[19] == 'Cancel_Goods_Receipt':
            Cancel_Goods_Receipt.append(c[19])
        if c[19] == 'SRM_Transfer_Failed_ESys':
            SRM_Transfer_Failed_ESys.append(c[19])
        if c[19] == 'Set_Payment_Block':
            Set_Payment_Block.append(c[19])
        if c[19] == 'Change_Quantity':
            Change_Quantity.append(c[19])
        if c[19] == 'Change_Delivery_Indicator':
            Change_Delivery_Indicator.append(c[19])
        if c[19] == 'Change_Approval_for_Purchase_Order':
            Change_Approval_for_Purchase_Order.append(c[19])
        if c[19] == 'Delete_Purchase_Order_Item':
            Delete_Purchase_Order_Item.append(c[19])
        if c[19] == 'Cancel_Subsequent_Invoice':
            Cancel_Subsequent_Invoice.append(c[19])
        if c[19] == 'Create_Purchase_Requisition_Item':
            Create_Purchase_Requisition_Item.append(c[19])
        if c[19] == 'Receive_Order_Confirmation':
            Receive_Order_Confirmation.append(c[19])
        if c[19] == 'Record_Subsequent_Invoice':
            Record_Subsequent_Invoice.append(c[19])
        if c[19] == 'SRM_Transaction_Completed':
            SRM_Transaction_Completed.append(c[19])
        if c[19] == 'Change_Final_Invoice_Indicator':
            Change_Final_Invoice_Indicator.append(c[19])
        if c[19] == 'SRM_Held':
            SRM_Held.append(c[19])
        if c[19] == 'SRM_Incomplete':
            SRM_Incomplete.append(c[19])
        if c[19] == 'Reactivate_Purchase_Order_Item':
            Reactivate_Purchase_Order_Item.append(c[19])
        if c[19] == 'Change_Rejection_Indicator':
            Change_Rejection_Indicator.append(c[19])
        if c[19] == 'Change_Storage_Location':
            Change_Storage_Location.append(c[19])
        if c[19] == 'Release_Purchase_Order':
            Release_Purchase_Order.append(c[19])
        if c[19] == 'Change_payment_term':
            Change_payment_term.append(c[19])

            #print(case_spendareatext)
        if c[17] == 'NONE':
            NONE.append(c[17])
        if c[17] == 'user_116':
            user_116.append(c[17])
        if c[17] == 'user_145':
            user_145.append(c[17])
        if c[17] == 'batch_00':
            batch_00.append(c[17])
        if c[17] == 'user_024':
            user_024.append(c[17])
        if c[17] == 'user_008':
            user_008.append(c[17])
        if c[17] == 'user_007':
            user_007.append(c[17])
        if c[17] == 'user_015':
            user_015.append(c[17])
        if c[17] == 'user_004':
            user_004.append(c[17])
        if c[17] == 'user_001':
            user_001.append(c[17])
        if c[17] == 'user_006':
            user_006.append(c[17])
        if c[17] == 'user_013':
            user_013.append(c[17])
        if c[17] == 'user_019':
            user_019.append(c[17])
        if c[17] == 'user_002':
            user_002.append(c[17])
        if c[17] == 'user_020':
            user_020.append(c[17])
        if c[17] == 'user_012':
            user_012.append(c[17])
        if c[17] == 'batch_02':
            batch_02.append(c[17])
        if c[17] == 'user_000':
            user_000.append(c[17])
        if c[17] == 'user_005':
            user_005.append(c[17])
        if c[17] == 'user_003':
            user_003.append(c[17])
        if c[17] == 'user_063':
            user_063.append(c[17])
        if c[17] == 'user_177':
            user_177.append(c[17])
        if c[17] == 'user_197':
            user_197.append(c[17])
        if c[17] == 'user_038':
            user_038.append(c[17])
        if c[17] == 'user_029':
            user_029.append(c[17])
        if c[17] == 'user_266':
            user_266.append(c[17])
        if c[17] == 'user_267':
            user_267.append(c[17])
        if c[17] == 'user_073':
            user_073.append(c[17])
        if c[17] == 'user_011':
            user_011.append(c[17])
        if c[17] == 'user_014':
            user_014.append(c[17])
        if c[17] == 'user_016':
            user_016.append(c[17])
        if c[17] == 'user_027':
            user_027.append(c[17])
        if c[17] == 'user_010':
            user_010.append(c[17])
        if c[17] == 'user_091':
            user_091.append(c[17])
        if c[17] == 'user_206':
            user_206.append(c[17])
        if c[17] == 'user_098':
            user_098.append(c[17])
        if c[17] == 'user_092':
            user_092.append(c[17])
        if c[17] == 'user_110':
            user_110.append(c[17])
        if c[17] == 'user_018':
            user_018.append(c[17])
        if c[17] == 'user_111':
            user_111.append(c[17])
        if c[17] == 'user_112':
            user_112.append(c[17])
        if c[17] == 'user_160':
            user_160.append(c[17])
        if c[17] == 'user_161':
            user_161.append(c[17])
        if c[17] == 'user_140':
            user_140.append(c[17])
        if c[17] == 'user_023':
            user_023.append(c[17])
        if c[17] == 'user_083':
            user_083.append(c[17])
        if c[17] == 'user_201':
            user_201.append(c[17])
        if c[17] == 'user_203':
            user_203.append(c[17])
        if c[17] == 'user_235':
            user_235.append(c[17])
        if c[17] == 'user_084':
            user_084.append(c[17])
        if c[17] == 'user_131':
            user_131.append(c[17])
        if c[17] == 'user_132':
            user_132.append(c[17])
        if c[17] == 'user_156':
            user_156.append(c[17])
        if c[17] == 'user_200':
            user_200.append(c[17])
        if c[17] == 'user_147':
            user_147.append(c[17])
        if c[17] == 'user_130':
            user_130.append(c[17])
        if c[17] == 'user_223':
            user_223.append(c[17])
        if c[17] == 'user_273':
            user_273.append(c[17])
        if c[17] == 'user_165':
            user_165.append(c[17])
        if c[17] == 'user_166':
            user_166.append(c[17])
        if c[17] == 'user_059':
            user_059.append(c[17])
        if c[17] == 'user_060':
            user_060.append(c[17])
        if c[17] == 'user_033':
            user_033.append(c[17])
        if c[17] == 'user_035':
            user_035.append(c[17])
        if c[17] == 'user_036':
            user_036.append(c[17])
        if c[17] == 'user_045':
            user_045.append(c[17])
        if c[17] == 'user_046':
            user_046.append(c[17])
        if c[17] == 'user_072':
            user_072.append(c[17])
        if c[17] == 'batch_06':
            batch_06.append(c[17])
        if c[17] == 'user_079':
            user_079.append(c[17])
        if c[17] == 'user_080':
            user_080.append(c[17])
        if c[17] == 'user_032':
            user_032.append(c[17])
        if c[17] == 'user_031':
            user_031.append(c[17])
        if c[17] == 'user_117':
            user_117.append(c[17])
        if c[17] == 'user_054':
            user_054.append(c[17])
        if c[17] == 'user_118':
            user_118.append(c[17])
        if c[17] == 'user_138':
            user_138.append(c[17])
        if c[17] == 'batch_01':
            batch_01.append(c[17])
        if c[17] == 'user_141':
            user_141.append(c[17])
        if c[17] == 'user_044':
            user_044.append(c[17])
        if c[17] == 'user_043':
            user_043.append(c[17])
        if c[17] == 'user_113':
            user_113.append(c[17])
        if c[17] == 'batch_10':
            batch_10.append(c[17])
        if c[17] == 'user_154':
            user_154.append(c[17])
        if c[17] == 'user_172':
            user_172.append(c[17])
        if c[17] == 'batch_12':
            batch_12.append(c[17])
        if c[17] == 'user_173':
            user_173.append(c[17])
        if c[17] == 'user_142':
            user_142.append(c[17])
        if c[17] == 'user_100':
            user_100.append(c[17])
        if c[17] == 'user_186':
            user_186.append(c[17])
        if c[17] == 'user_191':
            user_191.append(c[17])
        if c[17] == 'user_039':
            user_039.append(c[17])
        if c[17] == 'user_188':
            user_188.append(c[17])
        if c[17] == 'user_205':
            user_205.append(c[17])
        if c[17] == 'batch_07':
            batch_07.append(c[17])
        if c[17] == 'user_070':
            user_070.append(c[17])
        if c[17] == 'user_202':
            user_202.append(c[17])
        if c[17] == 'user_124':
            user_124.append(c[17])
        if c[17] == 'user_009':
            user_009.append(c[17])
        if c[17] == 'user_017':
            user_017.append(c[17])
        if c[17] == 'user_040':
            user_040.append(c[17])
        if c[17] == 'user_164':
            user_164.append(c[17])
        if c[17] == 'user_216':
            user_216.append(c[17])
        if c[17] == 'user_192':
            user_192.append(c[17])
        if c[17] == 'user_198':
            user_198.append(c[17])
        if c[17] == 'user_208':
            user_208.append(c[17])
        if c[17] == 'user_222':
            user_222.append(c[17])
        if c[17] == 'user_144':
            user_144.append(c[17])
        if c[17] == 'user_228':
            user_228.append(c[17])
        if c[17] == 'user_094':
            user_094.append(c[17])
        if c[17] == 'batch_08':
            batch_08.append(c[17])
        if c[17] == 'user_042':
            user_042.append(c[17])
        if c[17] == 'user_047':
            user_047.append(c[17])
        if c[17] == 'user_068':
            user_068.append(c[17])
        if c[17] == 'user_207':
            user_207.append(c[17])
        if c[17] == 'user_146':
            user_146.append(c[17])
        if c[17] == 'user_249':
            user_249.append(c[17])
        if c[17] == 'user_021':
            user_021.append(c[17])
        if c[17] == 'user_218':
            user_218.append(c[17])
        if c[17] == 'user_034':
            user_034.append(c[17])
        if c[17] == 'user_122':
            user_122.append(c[17])
        if c[17] == 'user_064':
            user_064.append(c[17])
        if c[17] == 'user_022':
            user_022.append(c[17])
        if c[17] == 'user_050':
            user_050.append(c[17])
        if c[17] == 'user_061':
            user_061.append(c[17])
        if c[17] == 'user_196':
            user_196.append(c[17])
        if c[17] == 'user_025':
            user_025.append(c[17])
        if c[17] == 'user_037':
            user_037.append(c[17])
        if c[17] == 'user_278':
            user_278.append(c[17])
        if c[17] == 'user_279':
            user_279.append(c[17])
        if c[17] == 'user_158':
            user_158.append(c[17])
        if c[17] == 'user_126':
            user_126.append(c[17])
        if c[17] == 'user_250':
            user_250.append(c[17])
        if c[17] == 'user_081':
            user_081.append(c[17])
        if c[17] == 'user_026':
            user_026.append(c[17])
        if c[17] == 'user_286':
            user_286.append(c[17])
        if c[17] == 'user_287':
            user_287.append(c[17])
        if c[17] == 'user_151':
            user_151.append(c[17])
        if c[17] == 'user_288':
            user_288.append(c[17])
        if c[17] == 'user_289':
            user_289.append(c[17])
        if c[17] == 'user_290':
            user_290.append(c[17])
        if c[17] == 'user_214':
            user_214.append(c[17])
        if c[17] == 'user_291':
            user_291.append(c[17])
        if c[17] == 'user_058':
            user_058.append(c[17])
        if c[17] == 'user_049':
            user_049.append(c[17])
        if c[17] == 'user_204':
            user_204.append(c[17])
        if c[17] == 'user_190':
            user_190.append(c[17])
        if c[17] == 'user_271':
            user_271.append(c[17])
        if c[17] == 'user_171':
            user_171.append(c[17])
        if c[17] == 'user_087':
            user_087.append(c[17])
        if c[17] == 'user_303':
            user_303.append(c[17])
        if c[17] == 'user_304':
            user_304.append(c[17])
        if c[17] == 'user_194':
            user_194.append(c[17])
        if c[17] == 'user_102':
            user_102.append(c[17])
        if c[17] == 'user_086':
            user_086.append(c[17])
        if c[17] == 'user_251':
            user_251.append(c[17])
        if c[17] == 'user_048':
            user_048.append(c[17])
        if c[17] == 'user_066':
            user_066.append(c[17])
        if c[17] == 'user_088':
            user_088.append(c[17])
        if c[17] == 'user_152':
            user_152.append(c[17])
        if c[17] == 'user_163':
            user_163.append(c[17])
        if c[17] == 'user_077':
            user_077.append(c[17])
        if c[17] == 'user_071':
            user_071.append(c[17])
        if c[17] == 'user_119':
            user_119.append(c[17])
        if c[17] == 'user_028':
            user_028.append(c[17])
        if c[17] == 'user_187':
            user_187.append(c[17])
        if c[17] == 'user_099':
            user_099.append(c[17])
        if c[17] == 'user_325':
            user_325.append(c[17])
        if c[17] == 'user_294':
            user_294.append(c[17])
        if c[17] == 'user_336':
            user_336.append(c[17])
        if c[17] == 'user_337':
            user_337.append(c[17])
        if c[17] == 'user_180':
            user_180.append(c[17])
        if c[17] == 'batch_13':
            batch_13.append(c[17])
        if c[17] == 'user_057':
            user_057.append(c[17])
        if c[17] == 'user_169':
            user_169.append(c[17])
        if c[17] == 'user_211':
            user_211.append(c[17])
        if c[17] == 'user_125':
            user_125.append(c[17])
        if c[17] == 'user_262':
            user_262.append(c[17])
        if c[17] == 'user_339':
            user_339.append(c[17])
        if c[17] == 'user_308':
            user_308.append(c[17])
        if c[17] == 'user_362':
            user_362.append(c[17])
        if c[17] == 'user_340':
            user_340.append(c[17])
        if c[17] == 'user_365':
            user_365.append(c[17])
        if c[17] == 'user_105':
            user_105.append(c[17])
        if c[17] == 'user_299':
            user_299.append(c[17])
        if c[17] == 'user_306':
            user_306.append(c[17])
        if c[17] == 'user_115':
            user_115.append(c[17])
        if c[17] == 'user_127':
            user_127.append(c[17])
        if c[17] == 'user_272':
            user_272.append(c[17])
        if c[17] == 'user_256':
            user_256.append(c[17])
        if c[17] == 'user_396':
            user_396.append(c[17])
        if c[17] == 'user_136':
            user_136.append(c[17])
        if c[17] == 'user_178':
            user_178.append(c[17])
        if c[17] == 'user_121':
            user_121.append(c[17])
        if c[17] == 'batch_11':
            batch_11.append(c[17])
        if c[17] == 'user_380':
            user_380.append(c[17])
        if c[17] == 'user_382':
            user_382.append(c[17])
        if c[17] == 'user_364':
            user_364.append(c[17])
        if c[17] == 'user_353':
            user_353.append(c[17])
        if c[17] == 'user_360':
            user_360.append(c[17])
        if c[17] == 'user_243':
            user_243.append(c[17])
        if c[17] == 'user_385':
            user_385.append(c[17])
        if c[17] == 'user_322':
            user_322.append(c[17])
        if c[17] == 'user_264':
            user_264.append(c[17])
        if c[17] == 'user_387':
            user_387.append(c[17])
        if c[17] == 'user_078':
            user_078.append(c[17])
        if c[17] == 'user_341':
            user_341.append(c[17])
        if c[17] == 'user_137':
            user_137.append(c[17])
        if c[17] == 'user_417':
            user_417.append(c[17])
        if c[17] == 'user_101':
            user_101.append(c[17])
        if c[17] == 'user_082':
            user_082.append(c[17])
        if c[17] == 'user_402':
            user_402.append(c[17])
        if c[17] == 'user_300':
            user_300.append(c[17])
        if c[17] == 'user_258':
            user_258.append(c[17])
        if c[17] == 'user_335':
            user_335.append(c[17])
        if c[17] == 'user_332':
            user_332.append(c[17])
        if c[17] == 'user_397':
            user_397.append(c[17])
        if c[17] == 'user_372':
            user_372.append(c[17])
        if c[17] == 'user_333':
            user_333.append(c[17])
        if c[17] == 'batch_15':
            batch_15.append(c[17])
        if c[17] == 'user_427':
            user_427.append(c[17])
        if c[17] == 'user_075':
            user_075.append(c[17])
        if c[17] == 'user_238':
            user_238.append(c[17])
        if c[17] == 'user_451':
            user_451.append(c[17])
        if c[17] == 'user_453':
            user_453.append(c[17])
        if c[17] == 'user_486':
            user_486.append(c[17])
        if c[17] == 'user_480':
            user_480.append(c[17])
        if c[17] == 'user_421':
            user_421.append(c[17])
        if c[17] == 'user_374':
            user_374.append(c[17])
        if c[17] == 'batch_16':
            batch_16.append(c[17])
        if c[17] == 'user_320':
            user_320.append(c[17])
        if c[17] == 'user_500':
            user_500.append(c[17])
        if c[17] == 'user_319':
            user_319.append(c[17])
        if c[17] == 'user_440':
            user_440.append(c[17])
        if c[17] == 'user_439':
            user_439.append(c[17])
        if c[17] == 'user_524':
            user_524.append(c[17])
        if c[17] == 'user_538':
            user_538.append(c[17])
        if c[17] == 'user_373':
            user_373.append(c[17])
        if c[17] == 'batch_17':
            batch_17.append(c[17])
        if c[17] == 'user_549':
            user_549.append(c[17])
        if c[17] == 'user_464':
            user_464.append(c[17])
        if c[17] == 'user_123':
            user_123.append(c[17])
        if c[17] == 'user_392':
            user_392.append(c[17])
        if c[17] == 'user_424':
            user_424.append(c[17])
        if c[17] == 'user_212':
            user_212.append(c[17])
        if c[17] == 'user_461':
            user_461.append(c[17])
        if c[17] == 'user_481':
            user_481.append(c[17])
        if c[17] == 'user_220':
            user_220.append(c[17])
        if c[17] == 'user_556':
            user_556.append(c[17])
        if c[17] == 'user_093':
            user_093.append(c[17])
        if c[17] == 'user_470':
            user_470.append(c[17])
        if c[17] == 'user_085':
            user_085.append(c[17])
        if c[17] == 'user_444':
            user_444.append(c[17])
        if c[17] == 'user_590':
            user_590.append(c[17])
        if c[17] == 'user_363':
            user_363.append(c[17])
        if c[17] == 'user_381':
            user_381.append(c[17])
        if c[17] == 'user_305':
            user_305.append(c[17])
        if c[17] == 'user_224':
            user_224.append(c[17])
        if c[17] == 'batch_18':
            batch_18.append(c[17])
        if c[17] == 'user_309':
            user_309.append(c[17])
        if c[17] == 'user_358':
            user_358.append(c[17])
        if c[17] == 'user_601':
            user_601.append(c[17])

            #end of checks

        #print(len(batch_00))
        #print(c[19])
        if c[19] == "Create_Purchase_Order_Item":
            count_processstart.append(c[19])
        if c[19] == "Clear_Invoice":
            count_processend.append(c[19])

        if c[17] not in count_users:                   #Remove NONE from data i chose to kanskje fjerne denne? og bare legge til none i egen liste?
            count_users.append(c[17])
        if c[19] not in count_activities: #add to activities
            count_activities.append(c[19])
        if timechecker > time_max: #finding time_max
            time_max = timechecker
        if timechecker < time_min: # finding time_min
            time_min = timechecker
            #print("skal finne minium")
    througputtime = time_max - time_min #defining all the variables
    #print(count_activities)

    count_activities = len(count_activities)
    
    count_users = len(count_users)
    count_processstart = len(count_processstart)
    count_processend = len(count_processend)

    #print(case_name)
    case = [case_name, case_spendareatext, case_company, count_processstart, count_processend, count_activities, count_events, count_users, count_ordervalue, case_document_type, case_sub_spend, case_purch_doc, case_vendor, case_item_type, case_item_category, case_spend_class, case_source, case_name_first, case_GR, case_item, case_goods_recieved, len(NONE), len(user_116), len(user_145), len(batch_00), len(user_024), len(user_008), len(user_007), len(user_015), len(user_004), len(user_001), len(user_006), len(user_013), len(user_019), len(user_002), len(user_020), len(user_012), len(batch_02), len(user_000), len(user_005), len(user_003), len(user_063), len(user_177), len(user_197), len(user_038), len(user_029), len(user_266), len(user_267), len(user_073), len(user_011), len(user_014), len(user_016), len(user_027), len(user_010), len(user_091), len(user_206), len(user_098), len(user_092), len(user_110), len(user_018), len(user_111), len(user_112), len(user_160), len(user_161), len(user_140), len(user_023), len(user_083), len(user_201), len(user_203), len(user_235), len(user_084), len(user_131), len(user_132), len(user_156), len(user_200), len(user_147), len(user_130), len(user_223), len(user_273), len(user_165), len(user_166), len(user_059), len(user_060), len(user_033), len(user_035), len(user_036), len(user_045), len(user_046), len(user_072), len(batch_06), len(user_079), len(user_080), len(user_032), len(user_031), len(user_117), len(user_054), len(user_118), len(user_138), len(batch_01), len(user_141), len(user_044), len(user_043), len(user_113), len(batch_10), len(user_154), len(user_172), len(batch_12), len(user_173), len(user_142), len(user_100), len(user_186), len(user_191), len(user_039), len(user_188), len(user_205), len(batch_07), len(user_070), len(user_202), len(user_124), len(user_009), len(user_017), len(user_040), len(user_164), len(user_216), len(user_192), len(user_198), len(user_208), len(user_222), len(user_144), len(user_228), len(user_094), len(batch_08), len(user_042), len(user_047), len(user_068), len(user_207), len(user_146), len(user_249), len(user_021), len(user_218), len(user_034), len(user_122), len(user_064), len(user_022), len(user_050), len(user_061), len(user_196), len(user_025), len(user_037), len(user_278), len(user_279), len(user_158), len(user_126), len(user_250), len(user_081), len(user_026), len(user_286), len(user_287), len(user_151), len(user_288), len(user_289), len(user_290), len(user_214), len(user_291), len(user_058), len(user_049), len(user_204), len(user_190), len(user_271), len(user_171), len(user_087), len(user_303), len(user_304), len(user_194), len(user_102), len(user_086), len(user_251), len(user_048), len(user_066), len(user_088), len(user_152), len(user_163), len(user_077), len(user_071), len(user_119), len(user_028), len(user_187), len(user_099), len(user_325), len(user_294), len(user_336), len(user_337), len(user_180), len(batch_13), len(user_057), len(user_169), len(user_211), len(user_125), len(user_262), len(user_339), len(user_308), len(user_362), len(user_340), len(user_365), len(user_105), len(user_299), len(user_306), len(user_115), len(user_127), len(user_272), len(user_256), len(user_396), len(user_136), len(user_178), len(user_121), len(batch_11), len(user_380), len(user_382), len(user_364), len(user_353), len(user_360), len(user_243), len(user_385), len(user_322), len(user_264), len(user_387), len(user_078), len(user_341), len(user_137), len(user_417), len(user_101), len(user_082), len(user_402), len(user_300), len(user_258), len(user_335), len(user_332), len(user_397), len(user_372), len(user_333), len(batch_15), len(user_427), len(user_075), len(user_238), len(user_451), len(user_453), len(user_486), len(user_480), len(user_421), len(user_374), len(batch_16), len(user_320), len(user_500), len(user_319), len(user_440), len(user_439), len(user_524), len(user_538), len(user_373), len(batch_17), len(user_549), len(user_464), len(user_123), len(user_392), len(user_424), len(user_212), len(user_461), len(user_481), len(user_220), len(user_556), len(user_093), len(user_470), len(user_085), len(user_444), len(user_590), len(user_363), len(user_381), len(user_305), len(user_224), len(batch_18), len(user_309), len(user_358), len(user_601),len(Vendor_creates_debit_memo), len(Create_Purchase_Order_Item), len(Vendor_creates_invoice), len(Record_Service_Entry_Sheet), len(Record_Goods_Receipt), len(Record_Invoice_Receipt), len(Clear_Invoice), len(Cancel_Invoice_Receipt), len(Remove_Payment_Block), len(SRM_Created), len(SRM_Change_was_Transmitted), len(SRM_Complete), len(SRM_Awaiting_Approval), len(SRM_Document_Completed), len(SRM_In_Transfer_to_Execution_Syst), len(SRM_Ordered), len(Change_Price), len(SRM_Deleted), len(Cancel_Goods_Receipt), len(SRM_Transfer_Failed_ESys), len(Set_Payment_Block), len(Change_Quantity), len(Change_Delivery_Indicator), len(Change_Approval_for_Purchase_Order), len(Delete_Purchase_Order_Item), len(Cancel_Subsequent_Invoice), len(Create_Purchase_Requisition_Item), len(Receive_Order_Confirmation), len(Record_Subsequent_Invoice), len(SRM_Transaction_Completed), len(Change_Final_Invoice_Indicator), len(SRM_Held), len(SRM_Incomplete), len(Reactivate_Purchase_Order_Item), len(Change_Rejection_Indicator), len(Change_Storage_Location), len(Release_Purchase_Order), len(Change_payment_term),  througputtime]
    #listWithCasesPrepared.append(case)
    if count_activities >= 2 and count_processstart >= 1 and count_processend >=1:
        listWithCasesPrepared.append(case)





caselist =[]

listWithCases =[]

df = load_data_pandas("BPI_Filtered.csv")
#print(df)
#print(df["case concept:name"].nunique())
dfCase = df["case concept:name"]
#print(df["case concept:name"])
timeelapsed = 0
for line in dfCase:
    #print(line)
    caselist.append(line)

print("kommer hit")
dfList = df.values.tolist()
dfDict = df.to_dict()

#print(dfDict)
#print(len(dfList))
#print(dfList)
print("før unike")
caselist = unique_in_list(caselist)  #Finding the unique case numbers
print()
print(caselist)
thisdict = {}
print("kommerhit1")
print(len(caselist))
print(len(dfList))
for c in caselist:
    row = []
    for x in dfList:
        if c in x:
            #print("treffer")
            #print(x)
            row.append(x)
            #print("leser fra fil")
            #dfList.remove(x) #bør kanskje ikke ha med, men kan gjøre prosessen raskere
            #print(row)
    thisdict[c] = row

print("ferdig å lese fra fil")
makeVariables(thisdict)

dfobj = pd.DataFrame(listWithCasesPrepared, columns=['Case id', 'case spend area text', ' case company', 'n_processstarts', 'n_processends', 'n_activites', 'n_events', 'n_users', 'case_value','case_document_type', 'case_sub_spend', 'case_purch_doc', ' case_vendor','case_item_type', 'case_item_category', 'case_spend_class', 'case_source', 'case_name_first', 'case_GR', 'case_item', 'case_goods_recieved', ' NONE', ' user_116', ' user_145', ' batch_00', ' user_024', ' user_008', ' user_007', ' user_015', ' user_004', ' user_001', ' user_006', ' user_013', ' user_019', ' user_002', ' user_020', ' user_012', ' batch_02', ' user_000', ' user_005', ' user_003', ' user_063', ' user_177', ' user_197', ' user_038', ' user_029', ' user_266', ' user_267', ' user_073', ' user_011', ' user_014', ' user_016', ' user_027', ' user_010', ' user_091', ' user_206', ' user_098', ' user_092', ' user_110', ' user_018', ' user_111', ' user_112', ' user_160', ' user_161', ' user_140', ' user_023', ' user_083', ' user_201', ' user_203', ' user_235', ' user_084', ' user_131', ' user_132', ' user_156', ' user_200', ' user_147', ' user_130', ' user_223', ' user_273', ' user_165', ' user_166', ' user_059', ' user_060', ' user_033', ' user_035', ' user_036', ' user_045', ' user_046', ' user_072', ' batch_06', ' user_079', ' user_080', ' user_032', ' user_031', ' user_117', ' user_054', ' user_118', ' user_138', ' batch_01', ' user_141', ' user_044', ' user_043', ' user_113', ' batch_10', ' user_154', ' user_172', ' batch_12', ' user_173', ' user_142', ' user_100', ' user_186', ' user_191', ' user_039', ' user_188', ' user_205', ' batch_07', ' user_070', ' user_202', ' user_124', ' user_009', ' user_017', ' user_040', ' user_164', ' user_216', ' user_192', ' user_198', ' user_208', ' user_222', ' user_144', ' user_228', ' user_094', ' batch_08', ' user_042', ' user_047', ' user_068', ' user_207', ' user_146', ' user_249', ' user_021', ' user_218', ' user_034', ' user_122', ' user_064', ' user_022', ' user_050', ' user_061', ' user_196', ' user_025', ' user_037', ' user_278', ' user_279', ' user_158', ' user_126', ' user_250', ' user_081', ' user_026', ' user_286', ' user_287', ' user_151', ' user_288', ' user_289', ' user_290', ' user_214', ' user_291', ' user_058', ' user_049', ' user_204', ' user_190', ' user_271', ' user_171', ' user_087', ' user_303', ' user_304', ' user_194', ' user_102', ' user_086', ' user_251', ' user_048', ' user_066', ' user_088', ' user_152', ' user_163', ' user_077', ' user_071', ' user_119', ' user_028', ' user_187', ' user_099', ' user_325', ' user_294', ' user_336', ' user_337', ' user_180', ' batch_13', ' user_057', ' user_169', ' user_211', ' user_125', ' user_262', ' user_339', ' user_308', ' user_362', ' user_340', ' user_365', ' user_105', ' user_299', ' user_306', ' user_115', ' user_127', ' user_272', ' user_256', ' user_396', ' user_136', ' user_178', ' user_121', ' batch_11', ' user_380', ' user_382', ' user_364', ' user_353', ' user_360', ' user_243', ' user_385', ' user_322', ' user_264', ' user_387', ' user_078', ' user_341', ' user_137', ' user_417', ' user_101', ' user_082', ' user_402', ' user_300', ' user_258', ' user_335', ' user_332', ' user_397', ' user_372', ' user_333', ' batch_15', ' user_427', ' user_075', ' user_238', ' user_451', ' user_453', ' user_486', ' user_480', ' user_421', ' user_374', ' batch_16', ' user_320', ' user_500', ' user_319', ' user_440', ' user_439', ' user_524', ' user_538', ' user_373', ' batch_17', ' user_549', ' user_464', ' user_123', ' user_392', ' user_424', ' user_212', ' user_461', ' user_481', ' user_220', ' user_556', ' user_093', ' user_470', ' user_085', ' user_444', ' user_590', ' user_363', ' user_381', ' user_305', ' user_224', ' batch_18', ' user_309', ' user_358', ' user_601',' Vendor_creates_debit_memo', ' Create_Purchase_Order_Item', ' Vendor_creates_invoice', ' Record_Service_Entry_Sheet', ' Record_Goods_Receipt', ' Record_Invoice_Receipt', ' Clear_Invoice', ' Cancel_Invoice_Receipt', ' Remove_Payment_Block', ' SRM_Created', ' SRM_Change_was_Transmitted', ' SRM_Complete', ' SRM_Awaiting_Approval', ' SRM_Document_Completed', ' SRM_In_Transfer_to_Execution_Syst', ' SRM_Ordered', ' Change_Price', ' SRM_Deleted', ' Cancel_Goods_Receipt', ' SRM_Transfer_Failed_ESys', ' Set_Payment_Block', ' Change_Quantity', ' Change_Delivery_Indicator', ' Change_Approval_for_Purchase_Order', ' Delete_Purchase_Order_Item', ' Cancel_Subsequent_Invoice', ' Create_Purchase_Requisition_Item', ' Receive_Order_Confirmation', ' Record_Subsequent_Invoice', ' SRM_Transaction_Completed', ' Change_Final_Invoice_Indicator', ' SRM_Held', ' SRM_Incomplete', ' Reactivate_Purchase_Order_Item', ' Change_Rejection_Indicator', ' Change_Storage_Location', ' Release_Purchase_Order', ' Change_payment_term', 'time used:'])
#print(event_userids)
#print(dfobj)
dfobj.to_csv("casesWith2018.csv")


#print(len(thisdict.keys())))


