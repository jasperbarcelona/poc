from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import admin
from flask.ext.admin.contrib import sqla
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import Admin, BaseView, expose
import xlrd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ratmaxi8@127.0.0.1:3306/pldt'
db = SQLAlchemy(app)


class Problem(db.Model):
    __tablename__ = 'PROBLEMS'
    PROM_ID = db.Column(db.Integer, primary_key=True)
    PROM_REPORTED = db.Column(db.String(300))
    PROM_REPORTEDBY = db.Column(db.String(300))
    PROM_PRIORITY = db.Column(db.Integer())
    PROM_DESCRIPTION = db.Column(db.String(300))
    PROM_EMPE_ID = db.Column(db.String(300))
    PROM_WORG_NAME = db.Column(db.String(300))
    PROM_CONFIRMED = db.Column(db.String(300))
    PROM_CONFIRMEDBY = db.Column(db.String(300))
    PROM_CLEARED = db.Column(db.String(300))
    PROM_CLEAREDBY = db.Column(db.String(300))
    PROM_CAUSE = db.Column(db.String(300))
    PROM_ENTITY = db.Column(db.String(300))
    PROM_IMPACT = db.Column(db.String(300))
    PROM_ACKNOWLEDGED = db.Column(db.String(300))
    PROM_ACKNOWLEDGEDBY = db.Column(db.String(300))
    PROM_REGN_CODE = db.Column(db.String(300))
    PROM_MANS_NAME = db.Column(db.String(300))
    PROM_PLAT_ABBREVIATION = db.Column(db.String(300))
    PROM_CREATED = db.Column(db.String(300))
    PROM_CWORG_NAME = db.Column(db.String(300))
    PROM_NCCLOCATION = db.Column(db.String(300))
    PROM_NCCNETWORK1 = db.Column(db.String(300))
    PROM_NCCNETWORK2 = db.Column(db.String(300))
    PROM_NCCACTION = db.Column(db.String(300))
    PROM_NCCCAUSE = db.Column(db.String(300))
    PROM_PROM_NUMBER = db.Column(db.Integer())
    PROM_RELATION = db.Column(db.String(300))
    PROM_REPORTEDCONTACT = db.Column(db.String(300))
    PROM_PCAT_NAME = db.Column(db.String(300))
    PROM_CUST_REPORTED = db.Column(db.String(300))
    PROM_REASSIGNED = db.Column(db.String(300))
    PROM_REASSIGNEDBY = db.Column(db.String(300))
    PROM_AWORG_NAME = db.Column(db.String(300))
    PROM_TYPE = db.Column(db.String(300))
    PROM_PRSC_NAME = db.Column(db.String(300))
    PROM_ASSIGNEDTO = db.Column(db.String(300))
    PROM_KNOWLEDGEBASE = db.Column(db.String(300))

class ProblemAttribute(db.Model):
    __tablename__ = 'PROBLEM_ATTRIBUTES'
    PRAT_PROM_NUMBER = db.Column(db.Integer, primary_key=True)
    PRAT_PRAL_NAME = db.Column(db.String(300))
    PRAT_VALUE = db.Column(db.String(300))
    PRAT_OPTIONALITY = db.Column(db.String(300))
    PRAT_DISPLAYORDER = db.Column(db.Integer)
    PRAT_DATATYPE = db.Column(db.String(300))

class ServiceImplementationTask(db.Model):
    __tablename__ = 'SERVICE_IMPLEMENTATION_TASKS'
    SEIT_ID = db.Column(db.Integer, primary_key=True)
    SEOT_SERO_ID = db.Column(db.String(300))
    SEIT_SERO_REVISION = db.Column(db.Integer())
    SEOT_TIMING = db.Column(db.Integer())   
    SEIT_TASKNAME = db.Column(db.String(300))
    SEIT_STAS_ABBREVIATION = db.Column(db.String(300))
    SEIT_STATUSDATE = db.Column(db.String(300))
    SEIT_USERNAME = db.Column(db.String(300))
    SEIT_WORG_NAME = db.Column(db.String(300))
    SEIT_ASSIGNED = db.Column(db.String(300))
    SEIT_IMTL_WORKFLOW_FLAG = db.Column(db.String(300))
    SEIT_IMTL_TASKTYPE = db.Column(db.String(300))
    SEIT_PROPOSED_START_DATE = db.Column(db.String(300))
    SEIT_PROPOSED_END_DATE = db.Column(db.String(300))
    SEIT_ACTUAL_START_DATE = db.Column(db.String(300))
    SEIT_ACTUAL_END_DATE = db.Column(db.String(300))
    SEIT_IMTL_WORK_NAME = db.Column(db.String(300))
    SEIT_IMTL_FUNCTION = db.Column(db.String(300))
    SEIT_WF_ITEMTYPE = db.Column(db.String(300))
    SEIT_WF_ITEMKEY = db.Column(db.String(300))
    SEIT_WF_ACTID = db.Column(db.Integer())
    SEIT_IMTL_WOPR_NAME = db.Column(db.String(300))
    SEIT_DISPLAY_ORDER = db.Column(db.Integer())
    SEIT_ESCALATION_DATE = db.Column(db.String(300))
    SEIT_EMPE_ID = db.Column(db.String(300))
    SEIT_CALLEDTYPE = db.Column(db.String(300))
    SEIT_CALLEDKEY = db.Column(db.String(300))
    SEIT_RETRIED = db.Column(db.Integer())

class ServiceOrder(db.Model):
    __tablename__ = 'SERVICE_ORDERS'
    SERO_ID = db.Column(db.String(200), primary_key=True)
    SERO_REVISION = db.Column(db.Integer())
    SERO_CUSR_ABBREVIATION = db.Column(db.String(300))
    SERO_ACCT_NUMBER = db.Column(db.String(300))
    SERO_SEOP_PRIORITY = db.Column(db.String(300))
    SERO_WORG_NAME = db.Column(db.String(300))
    SERO_LOCN_ID_AEND = db.Column(db.Integer())
    SERO_LOCN_ID_BEND = db.Column(db.Integer())
    SERO_ORDT_TYPE = db.Column(db.String(300))
    SERO_STAS_ABBREVIATION = db.Column(db.String(300))
    SERO_STATUSDATE = db.Column(db.String(300))
    SERO_SERT_ABBERVIATION = db.Column(db.String(300))
    SERO_SPED_ABBREVIATION = db.Column(db.String(300))
    SERP_TRAT_APPLICATION = db.Column(db.String(300))
    SERO_CONTRACTNO = db.Column(db.String(300))
    SERO_CIRT_NAME = db.Column(db.String(300))
    SERO_DATECREATED = db.Column(db.String(300))
    SERO_USERCREATED = db.Column(db.String(300))
    SERO_OEID = db.Column(db.String(300))
    SERO_STAS_REASON = db.Column(db.String(300))
    SERO_PROJECTID = db.Column(db.String(300))
    SERO_CREQ_CSRFNO = db.Column(db.String(300))
    SERO_CREQ_REQUESTNO = db.Column(db.String(300))
    SERO_WF_ITEMTYPE = db.Column(db.String(300))
    SERO_WF_ITEMKEY = db.Column(db.String(300))
    SERO_WF_USERKEY = db.Column(db.String(300))
    SERO_CIRT_COUNT = db.Column(db.Integer())
    SERO_ADDE_ID_BEND = db.Column(db.Integer())
    SERO_ADDE_ID_AEND = db.Column(db.Integer())
    SERO_SERV_ID = db.Column(db.String(300))
    SERO_AREA_CODE = db.Column(db.String(300))
    SERO_COMPLETION_DATE = db.Column(db.String(300))
    SERO_TRUG_ID = db.Column(db.Integer())
    SERO_SLAT_NAME = db.Column(db.String(300))
    SERO_ESCALATION_DATE = db.Column(db.String(300))
    SERO_SERO_ID = db.Column(db.String(300))
    SERO_SERV_DISPLAYNAME = db.Column(db.String(300))
    SERO_SEIT_ID = db.Column(db.Integer())

class ServiceOrderAttribute(db.Model):
    __tablename__ = 'SERVICE_ORDER_ATTRIBUTES'
    SEOA_ID = db.Column(db.Integer, primary_key=True)
    SEOA_NAME = db.Column(db.String(300))
    SEOA_SERO_ID = db.Column(db.String(300))
    SEOA_SERO_REVISION = db.Column(db.Integer())
    SEOA_DEFAULTVALUE = db.Column(db.String(300))
    SEOA_DISPLAY_ORDER = db.Column(db.Integer())
    SEOA_PREV_VALUE = db.Column(db.String(300))
    SEOA_SOFE_ID = db.Column(db.Integer())
    SEOA_HIDDEN = db.Column(db.String(300))

class IngAdmin(sqla.ModelView):
    column_display_pk = True
    column_edit_pk = True

admin = Admin(app, name='creatdb')
admin.add_view(IngAdmin(Problem, db.session))
admin.add_view(IngAdmin(ProblemAttribute, db.session))
admin.add_view(IngAdmin(ServiceImplementationTask, db.session))
admin.add_view(IngAdmin(ServiceOrder, db.session))
admin.add_view(IngAdmin(ServiceOrderAttribute, db.session))

def open_file(path,table,rows,cols):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)
 
    # get the first worksheet
    sheet = book.sheet_by_index(0)
 
    for row in range(rows-1):
        vals = []
        for col in range(cols):
            cell = sheet.cell(row+1,col)
            if cell.value == '':
                vals.append(None)
            else:
                vals.append(cell.value)

        if table == 'problem_attributes':
            new_record = ProblemAttribute(
                PRAT_PROM_NUMBER=vals[0],
                PRAT_PRAL_NAME=vals[1],
                PRAT_VALUE=vals[2],
                PRAT_OPTIONALITY=vals[3],
                PRAT_DISPLAYORDER=vals[4],
                PRAT_DATATYPE=vals[5]
                )
            db.session.add(new_record)

        elif table == 'service_order_attributes':
            new_record = ServiceOrderAttribute(
                SEOA_ID=vals[0],
                SEOA_NAME=vals[1],
                SEOA_SERO_ID=vals[2],
                SEOA_SERO_REVISION=vals[3],
                SEOA_DEFAULTVALUE=vals[4],
                SEOA_DISPLAY_ORDER=vals[5],
                SEOA_PREV_VALUE=vals[6],
                SEOA_SOFE_ID=vals[7],
                SEOA_HIDDEN=vals[8]
                )
            db.session.add(new_record)

        elif table == 'service_orders':
            new_record = ServiceOrder(
                SERO_ID=vals[0],
                SERO_REVISION=vals[1],
                SERO_CUSR_ABBREVIATION=vals[2],
                SERO_ACCT_NUMBER=vals[3],
                SERO_SEOP_PRIORITY=vals[4],
                SERO_WORG_NAME=vals[5],
                SERO_LOCN_ID_AEND=vals[6],
                SERO_LOCN_ID_BEND=vals[7],
                SERO_ORDT_TYPE=vals[8],
                SERO_STAS_ABBREVIATION=vals[9],
                SERO_STATUSDATE=vals[10],
                SERO_SERT_ABBERVIATION=vals[11],
                SERO_SPED_ABBREVIATION=vals[12],
                SERP_TRAT_APPLICATION=vals[13],
                SERO_CONTRACTNO=vals[14],
                SERO_CIRT_NAME=vals[15],
                SERO_DATECREATED=vals[16],
                SERO_USERCREATED=vals[17],
                SERO_OEID=vals[18],
                SERO_STAS_REASON=vals[19],
                SERO_PROJECTID=vals[20],
                SERO_CREQ_CSRFNO=vals[21],
                SERO_CREQ_REQUESTNO=vals[22],
                SERO_WF_ITEMTYPE=vals[23],
                SERO_WF_ITEMKEY=vals[24],
                SERO_WF_USERKEY=vals[25],
                SERO_CIRT_COUNT=vals[26],
                SERO_ADDE_ID_BEND=vals[27],
                SERO_ADDE_ID_AEND=vals[28],
                SERO_SERV_ID=vals[29],
                SERO_AREA_CODE=vals[30],
                SERO_COMPLETION_DATE=vals[31],
                SERO_TRUG_ID=vals[32],
                SERO_SLAT_NAME=vals[33],
                SERO_ESCALATION_DATE=vals[34],
                SERO_SERO_ID=vals[35],
                SERO_SERV_DISPLAYNAME=vals[36],
                SERO_SEIT_ID=vals[37]
                )
            db.session.add(new_record)

        elif table == 'service_implementation_tasks':
            new_record = ServiceImplementationTask(
                SEIT_ID=vals[0],
                SEOT_SERO_ID=vals[1],
                SEIT_SERO_REVISION=vals[2],
                SEOT_TIMING=vals[3],
                SEIT_TASKNAME=vals[4],
                SEIT_STAS_ABBREVIATION=vals[5],
                SEIT_STATUSDATE=vals[6],
                SEIT_USERNAME=vals[7],
                SEIT_WORG_NAME=vals[8],
                SEIT_ASSIGNED=vals[9],
                SEIT_IMTL_WORKFLOW_FLAG=vals[10],
                SEIT_IMTL_TASKTYPE=vals[11],
                SEIT_PROPOSED_START_DATE=vals[12],
                SEIT_PROPOSED_END_DATE=vals[13],
                SEIT_ACTUAL_START_DATE=vals[14],
                SEIT_ACTUAL_END_DATE=vals[15],
                SEIT_IMTL_WORK_NAME=vals[16],
                SEIT_IMTL_FUNCTION=vals[17],
                SEIT_WF_ITEMTYPE=vals[18],
                SEIT_WF_ITEMKEY=vals[19],
                SEIT_WF_ACTID=vals[20],
                SEIT_IMTL_WOPR_NAME=vals[21],
                SEIT_DISPLAY_ORDER=vals[22],
                SEIT_ESCALATION_DATE=vals[23],
                SEIT_EMPE_ID=vals[24],
                SEIT_CALLEDTYPE=vals[25],
                SEIT_CALLEDKEY=vals[26],
                SEIT_RETRIED=vals[27]
                )
            db.session.add(new_record)

        elif table == 'problems':
            new_record = Problem(
                PROM_ID=vals[0],
                PROM_REPORTED=vals[1],
                PROM_REPORTEDBY=vals[2],
                PROM_PRIORITY=vals[3],
                PROM_DESCRIPTION=vals[4],
                PROM_EMPE_ID=vals[5],
                PROM_WORG_NAME=vals[6],
                PROM_CONFIRMED=vals[7],
                PROM_CONFIRMEDBY=vals[8],
                PROM_CLEARED=vals[9],
                PROM_CLEAREDBY=vals[10],
                PROM_CAUSE=vals[11],
                PROM_ENTITY=vals[12],
                PROM_IMPACT=vals[13],
                PROM_ACKNOWLEDGED=vals[14],
                PROM_ACKNOWLEDGEDBY=vals[15],
                PROM_REGN_CODE=vals[16],
                PROM_MANS_NAME=vals[17],
                PROM_PLAT_ABBREVIATION=vals[18],
                PROM_CREATED=vals[19],
                PROM_CWORG_NAME=vals[20],
                PROM_NCCLOCATION=vals[21],
                PROM_NCCNETWORK1=vals[22],
                PROM_NCCNETWORK2=vals[23],
                PROM_NCCACTION=vals[24],
                PROM_NCCCAUSE=vals[25],
                PROM_PROM_NUMBER=vals[26],
                PROM_RELATION=vals[27],
                PROM_REPORTEDCONTACT=vals[28],
                PROM_PCAT_NAME=vals[29],
                PROM_CUST_REPORTED=vals[30],
                PROM_REASSIGNED=vals[31],
                PROM_REASSIGNEDBY=vals[32],
                PROM_AWORG_NAME=vals[33],
                PROM_TYPE=vals[34],
                PROM_PRSC_NAME=vals[35],
                PROM_ASSIGNEDTO=vals[36],
                PROM_KNOWLEDGEBASE=vals[37]
                )
            db.session.add(new_record)
        db.session.commit()
    print('xxxxxxxxxxxxxxxxxxxxxxx')
    print('DONE')
    return

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    open_file('/pldt_xls/PROBLEM_ATTRIBUTES.xls','problem_attributes',2,6)
    open_file('/pldt_xls/SERVICE_ORDER_ATTRIBUTES.xls','service_order_attributes',81,9)
    open_file('/pldt_xls/SERVICE_ORDERS.xls','service_orders',2,38)
    open_file('/pldt_xls/SERVICE_IMPLEMENTATION_TASKS.xls','service_implementation_tasks',4,28)
    open_file('/pldt_xls/PROBLEMS.xls','problems',2,38)
    app.run()