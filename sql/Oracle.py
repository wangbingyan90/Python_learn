import cx_Oracle                                    #引用模块cx_Oracle

conn=cx_Oracle.connect('NCC8311/1@172.16.72.122:1521/pdborcl')    #连接数据库 用户名/密码@主机ip地址/orcl

cursor = conn.cursor()                                        #获取cursor


# sql = "INSERT INTO fipub_timecontrol (ts, ordertype, code, timectrlname2, creator, modifier, creationtime, timectrlname3, timectrlname4, unit, timectrlname5, timectrlname, timectrlname6, days, pk_org, modifiedtime, pk_group, scomment, pk_timectrl, dr ) VALUES ('2019-01-15 10:10:34', 0, '003', null, '1001A3100000000IHCW7', '~', '2019-01-15 10:10:33', null, null, 0, null, '003a', null, 0, '0001A1100000000005NL', null, '0001A1100000000005NL', null, '1001A3100000000MMIJE', 0 )"
# cursor.execute(sql)
# sql = "insert into gl_transproject (ts, pk_transproject, transprojectname, transprojectcode, memo, pk_accountingbook, pk_group, pk_org, creator, creationtime, pk_unit ) values ('2019-01-15 13:24:36', '1002A1100000000051C0', '%d', '%d', '%d', '1001A110000000000C9V', null, null, null, null, null )"
# cursor.execute(sql)

'''
常用摘要-组织
for i in range(300,400):
    str1 = '1001A3100000000ML'+str(i)
    sql = "INSERT INTO fipub_summary ( pk_corp, ispublic, code, summaryname, creator, modifier, creationtime, pk_summary, pk_org, modifiedtime, pk_group, dr ) VALUES ( null, 'N', '%d', '%s', '1001A3100000000IHCW7', null, '2019-01-14 19:53:21', '%s', '0001A110000000000VUF', null, '0001A1100000000005NL', 0 )" % (i,str(i)+'摘要',str1)
    cursor.execute(sql)

'''


'''
科目关系设置-集团
for i in range(1,45):
    str1 = '1001A3100000000MKZ'+str(i)
    sql = "insert into gl_subrelation (ts, pk_subrelation, aspect, pk_cashflow, pk_org, pk_creditsubject, pk_debitsubject, scale, pk_sob, memo, pk_accountingbook, isDD, isCD, dfreevalueid, cfreevalueid, pk_unit, pk_setofbook, pk_group ) values ('2019-01-14 20:31:02', '%s', 0, '1001C1100000000BIEQH', '0001A1100000000005NL', '1001A11000000000094U', null, null, null, null, null, '', 'Y', null, null, null, '0001Z01000000000019Y', '0001A1100000000005NL' )" % (str1)
    cursor.execute(sql)
'''


'''
内部交易对账规则-集团
for i in range(700,807):
    str1 = '1001A3100000000ML'+str(i)
    sql = "insert into gl_contrastrule (ts, pk_contrastrule, code, name, contrastcontent, contrastmoney, createorg, creator, enddate, pk_book, pk_group, startdate, untallied, createtime, startstatus, crtelimvoucher, ismainorgcontrast ) values \
    ('2019-01-15 09:24:11', '%s', '%d', '%s', 'NNNNN', 'Y', '0001A1100000000005NL', null, null, '0001Z01000000000019Y', '0001A1100000000005NL', null, 'N', null, 0, 'Y', 'N' )" % (str1,i,str(i)+'名')
    cursor.execute(sql)

for i in range(208,461):
        str1 = '1001A3100000000ML'+str(i)
        sql = "delete from gl_contrastrule where pk_contrastrule = '%s'"%(str1)
        cursor.execute(sql)
'''


'''
账龄区间设置-集团
for i in range(100,200):
    str1 = '1001A3100000000MN'+str(i)
    sql = "INSERT INTO fipub_timecontrol (ts, ordertype, code, timectrlname2, creator, modifier, creationtime, timectrlname3, timectrlname4, unit, timectrlname5, timectrlname, timectrlname6, days, pk_org, modifiedtime, pk_group, scomment, pk_timectrl, dr ) VALUES ('2019-01-15 10:10:34', 0, '003', null, '1001A3100000000IHCW7', '~', '2019-01-15 10:10:33', null, null, 0, null, '003a', null, 0, '0001A1100000000005NL', null, '0001A1100000000005NL', null, '%s', 0 )" % (str1)
    cursor.execute(sql)
    sql = "INSERT INTO fipub_timecontrol_b (ts, endunit, pk_timectrl_b, startunit, sumunit, descr, propertyid, pk_timectrl, dr ) VALUES ('2019-01-15 10:10:34', null, '%s', null, null, 'aa', 1, '%s', 0 )" % (str1,str1)
    cursor.execute(sql)

# sql = "delete from fipub_timecontrol"
# cursor.execute(sql)
# sql = "delete from fipub_timecontrol_b"
# cursor.execute(sql)
'''



'''
协同凭证影响因素设置
for i in range(10,93):
    str1 = '1002A110000000004Y'+str(i)
    sql = "INSERT INTO gl_influecefactor (ts, jointype, entityid, detailfield, property, code, creator, modifier, creationtime, name5, name6, name3, pk_influecefactor, name4, pk_org, name, modifiedtime, pk_group, name2, dr ) VALUES ('2019-01-15 11:15:40', '1', 'BS000010000100001036', 'pk_detail', null, '%d', '1002A110000000001IXN', '~', '2019-01-15 11:15:40', null, null, null, '%s', null, '~', '%d', null, '~', null, 0 )" % (i,str1,i)
    cursor.execute(sql)
'''

'''
现金流量项目对照关系设置-集团
j = 10
for i in range(0,10):
    str1 = '111161'+str(i)
    for i in range(2,10):
        str2 = '11116'+str(i)
        str3 = '1001A3100000000MML'+str(j)
        j = j + 1
        sql = "INSERT INTO gl_cfitemrelation (ts, pk_cfitemrelation, descfitempk, creator, creationtime, modifier, srccfitempk, pk_org, modifiedtime, srccfitemcode, pk_group, descfitemcode, dr ) VALUES ('2019-01-15 11:44:13', '%s', '0001A11000000000091K', '1001A3100000000IHCW7', '2019-01-15 11:44:13', '~', '0001A110000000000921', '0001A1100000000005NL', null, '%s', '0001A1100000000005NL', '%s', 0 )" % (str3,str1,str2)
        cursor.execute(sql)
'''


#  pk_accountingbook = '1001A110000000000C9V' 账簿字段 : 贵安新区开发投资有限公司结算中心-基准账簿
'''
自定义结转方案档案定义
for i in range(100,201):
    str1 = '1002A110000000006'+str(i)
    sql = "insert into gl_transproject (ts, pk_transproject, transprojectname, transprojectcode, memo, pk_accountingbook, pk_group, pk_org, creator, creationtime, pk_unit ) values ('2019-01-15 13:24:36', '%s', '%d', '%d', '%d', '1001A110000000000C9V', null, null, null, null, null )" % (str1,i,i,i)
    cursor.execute(sql)
'''

'''
凭证类别-全局
for i in range(100,201):
    str1 = '1002A110000000006'+str(i)
    sql = "INSERT INTO bd_vouchertype (ts, shortname5, shortname6, shortname3, shortname4, description5, shortname2, description4, description6, description3, description2, dataoriginflag, creator, pk_currtype, pk_org, description, name, shortname, pk_vouchertype, dr, code, modifier, creationtime, name5, name6, name3, name4, modifiedtime, enablestate, pk_group, name2 ) VALUES ('2019-01-15 16:24:07', null, null, null, null, null, null, null, null, null, null, null, '1002A110000000001IB5', '~', 'GLOBLE00000000000000', null, '%s', '%s', '%s', 0, '%d', '~', '2019-01-15 16:24:07', null, null, null, null, null, 2, '0001A110000000003090', null )" %('凭证'+str(i),'简'+str(i),str1,i)
    cursor.execute(sql)
'''

'''
影响因素定义
for i in range(104,201):
    str1 = '1001A3100000000MN'+str(i)
    sql = "INSERT INTO fip_factor ( displayname3, displayname4, displayname2, indexid, entityid, pk_systypecode, displayformula, displayname5, displayname6, creator, creationtime, modifier, refmodelname, pk_org, modifiedtime, pk_group, displaytype, pk_factor, displaycode, displayname, dr ) VALUES ( null, null, null, null, 'BS000010000100001070', 'AIM', null, null, null, '1001A3100000000GJTVE', '2019-01-15 19:04:01', '~', '~', '~', null, '0001A1100000000005NL', null, '%s', null, '%d', 0 )"%(str1,i)
    cursor.execute(sql)
'''
'''
单据影响因素关联
for i in range(104,201):
    str1 = '1001A3100000000MN'+str(i)
    str2 = '1001A3100000000MN'+str(i)
    sql = "INSERT INTO fip_billfactor ( pk_systypecode, pk_billfactor, creator, modifier, creationtime, pk_org, entity_attr, modifiedtime, pk_factor, pk_group, dr, pk_billtype ) VALUES ( 'AIM', '%s', '1001A3100000000GJTVE', '~', '2019-01-15 19:20:35', '~', '$pk_record', null, '%s', '0001A1100000000005NL', 0, '4A54' )"%(str2,str1)
    cursor.execute(sql)
'''

'''
入账设置（规则）-集团
for i in range(104,201):
    str1 =  'getBD("fb4da7d4-77b0-4cb8-81c3-db65e32d63af","贵安新区开发投资有限公司-基准账簿","1001A110000000000C9Q")'
    str2 = '1001A3100000000MN'+str(i)
    sql = "INSERT INTO fip_orgrule ( sortindex, factorformula, pk_org, src_billtype, pk_group, des_billtype, pk_orgrule, factor3, orgformula, factor2, factor1, dr ) VALUES ( null, '%d', '~', '4A54', '0001A1100000000005NL', 'C0', '%s', '~','%s', '~', '~', 0 )"%(i,str2,str1)
    cursor.execute(sql)
'''


'''
入账设置对照-业务单元
for i in range(100,201):
    str1 = '1001A3100000000MN'+str(i)
    sql = "INSERT INTO fip_classdefine ( des_system, creator, pk_org, defaultvalue, dr, displayname3, displayname4, displayname2, pk_classview, pk_classfactor, src_billtype, pk_classdef, desdoctype, displayname5, displayname6, creationtime, modifier, iscopyfromgroup, pk_classmainprop, src_system, modifiedtime, des_billtype, pk_group, displaycode, displayname ) VALUES ( '', '1001A3100000000GJTVE', '1001A11000000000CAOV', '1001A110000000000C9Q', 0, null, null, null, '', '%s', '', '%s', 'fb4da7d4-77b0-4cb8-81c3-db65e32d63af', null, null, '2019-01-15 19:56:18', '', 'N', '~', 'AIM', null, 'C0', '0001A1100000000005NL', null, null )"%(str1,str1)
    cursor.execute(sql)
'''

'''
科目对照表-集团
for i in range(1000,1900):
    str1 = '1001A3100000000M'+str(i)
    sql = "INSERT INTO fip_docview ( pk_setorg1, desdocid, viewname, explanation6, explanation5, explanation4, explanation3, explanation2, creator, viewcode, pk_org, dr, viewname6, viewname4, viewname5, pk_classview, viewname2, viewname3, explanation, creationtime, modifier, orgtype, modifiedtime, pk_group ) VALUES ( '0001Z01000000000019Y', '407748f1-1fe8-4f0d-880e-ae8b0960308f', '%d', null, null, null, null, null, '1001A3100000000GJTVE', '%d', '0001A1100000000005NL', 0, null, null, null, '%s', null, null, null, '2019-01-15 20:13:54', '', '~', null, '0001A1100000000005NL' )"%(i,i,str1)
    cursor.execute(sql)
凭证类别约束规则-集团
for i in range(101,201):
    str1 = '1002A110000000006'+str(i)
    str2 = '1001A3100000000MN'+str(i)
    sql = "INSERT INTO fipub_vouchertyperule (ts, code, creator, modifier, creationtime, name5, name6, name3, ruletype, name4, pk_org, pk_vouchertyperule, name, pk_accountingbook, modifiedtime, pk_setofbook, pk_group, pk_vouchertype, name2, dr ) VALUES ('2019-01-15 20:34:53', '%d', '1001A3100000000GJTVE', '1001A3100000000GJTVE', '2019-01-15 20:34:53', null, null, null, '', null, '0001A1100000000005NL', '%s', '%d', '', '2019-01-15 20:34:53', '0001Z01000000000019Y', '', '%s', null, 0 )"%(i,str2,i,str1)
    cursor.execute(sql)
'''

  
insert into gl_docmap (ts, pk_docmap, pk_docmaptemplet, pk_srctype, pk_srcvalue, pk_destype, pk_desvalue, pk_docmaplink, def1, def2, def3, def4, def5, def7, def6, def8, def9, def10 ) values ('2019-01-17 11:49:55', '1001A3100000000MOARP', '1001A3100000000MOARO', 'BS000010000100001070', null, 'BS000010000100001070', null, null, null, null, null, null, null, null, null, null, null, null )

sql = ""




conn.commit()
cursor.close()                                                 #关闭cursor
conn.close()