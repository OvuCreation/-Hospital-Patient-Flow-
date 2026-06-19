import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import re
## loading the data
billing_df = pd.read_csv('billing(1).csv')
departbed_df = pd.read_csv('department_beds.csv')
dept = pd.read_csv('departments(1).csv')
diagnose_df = pd.read_csv('diagnoses(1).csv')
patient_df = pd.read_csv('patients(1).csv')
treatment_df = pd.read_csv('treatment_events.csv')

### data cleaning 
dept.info()

)
departbed_df['bed_status'].value_counts()
available = departbed_df[departbed_df['bed_status'] == 'Available']
print(f"Occupied: {len(available)}")
departbed_df.head(20)
treatment_df['event_datetime'] = pd.to_datetime(treatment_df['event_datetime'])
treatment_df['event_date'] = treatment_df['event_datetime'].dt.date
treatment_df['event_day'] = treatment_df['event_datetime'].dt.day_name
treatment_df = treatment_df.drop('event_day', axis=1)
treatment_df['event_hour'] = treatment_df['event_datetime'].dt.hour
treatment_df['event_month'] = treatment_df['event_datetime'].dt.month_name()
treatment_df['event_day'] = treatment_df['event_datetime'].dt.day_name()
treatment_df['event_year'] = treatment_df['event_datetime'].dt.year
treatment_df.head()
treatment_df['event_type'].value_counts()
admission_dff = pd.read_csv('admissions(1).csv')
patient_df.isnull().sum()
patient_df.duplicated()
patient_df.info()
patient_df['date_of_birth'] = pd.to_datetime(patient_df['date_of_birth'])
patient_df.head(5)
patient_df['full_name'].duplicated()




prefixes = ['070', '080', '090']

def clean_phone(num):
    if pd.isna(num):
        return None

    num = str(num)

  
    num = re.sub(r'x\d+', '', num, flags=re.IGNORECASE)

   
    num = re.sub(r'\D', '', num)

  
    num = num[-8:]


    if len(num) != 8:
        return None

    prefix = prefixes[hash(num) % len(prefixes)]

    return prefix + num





patient_df['contact_phone'] = (
    patient_df['contact_phone']
    .apply(clean_phone)
)
patient_df.head(5)




admission_dff.info()
admission_dff['admit_datetime'] = pd.to_datetime(admission_dff['admit_datetime'])

admission_dff['discharge_datetime'] = pd.to_datetime(admission_dff['discharge_datetime'])
type(admission_dff)
admission_dff['admit_date'] = admission_dff['discharge_datetime'].dt.date
admission_dff.head()
admission_dff = admission_dff.drop('admit_date',axis=1)



admission_dff.head()
admission_dff['admit_date'] = admission_dff['admit_datetime'].dt.date
admission_dff['admit_time'] = admission_dff['admit_datetime'].dt.time
admission_dff['discharge_date'] = admission_dff['discharge_datetime'].dt.date
admission_dff['discharge_time'] = admission_dff['discharge_datetime'].dt.time
admission_dff['discharge_date'].isna().sum()
mask = admission_dff['discharge_date'].isna() | admission_dff['discharge_time'].isna()
admission_dff[mask]
clone = admission_dff['admit_date'].isna() | admission_dff['admit_time'].isna()
admission_dff[clone]
admission_dff['admit_datetime'] = pd.to_datetime(
    admission_dff['admit_date'].astype(str) + ' ' +
    admission_dff['admit_time'].astype(str)
)


admission_dff['discharge_datetime'] = pd.to_datetime(
    admission_dff['discharge_date'].astype(str) + ' ' +
    admission_dff['discharge_time'].astype(str), errors="coerce"
)

admission_dff.head()
admission_dff['admit_date'].isna().sum()


#admission_dff = admission_dff.drop('admit_datetime', axis=1)
#admission_dff = admission_dff.drop('discharge_datetime', axis=1)


admission_dff.head()
admission_dff['outcome'].value_counts(dropna=False)
discharged = admission_dff[admission_dff['outcome'].str.contains("Discharged", case=False, na= False)].copy()

discharged['los_day']= (
    discharged['discharge_datetime'] -discharged['admit_datetime']
    ).dt.days

discharged.head(4)
discharged['los_days.second'] = (
    discharged['discharge_datetime'] - discharged['admit_datetime']
).dt.total_seconds() / 86400
discharged.head(2)
discharged.head(3)
discharged['los_day'].mean()


still_admitted= admission_dff[admission_dff['outcome'].str.contains("admitted", case=False, na= False)].copy()
patient_discharged = discharged.to_csv("patient_discharged.csv", index=False)
still_admitted['outcome'].count()
admission_dff.head(10)
admission_dff['admit_day'] = (
    admission_dff['admit_datetime'].dt.day_name()
)


admission_dff['discharge_day'] = (
    admission_dff['discharge_datetime'].dt.day_name())
admission_dff['admit_month'] = (
    admission_dff['admit_datetime'].dt.month_name())
admission_dff['discharge_month'] = (
    admission_dff['discharge_datetime'].dt.month_name())
admission_dff['currently_admitted'] = (
    admission_dff['discharge_datetime'].isna()
)

admission_dff.head(3)
patient_admission = admission_dff.to_csv('patient_admission.csv', index=False)
admission_dff = admission_dff.drop('admit_month', axis=1)
admission_dff['los'] = (
    admission_dff['admit_datetime'] - admission_dff['discharge_datetime']
)


admission_dff = admission_dff.drop('los', axis=1)
admission_dff['length_of_stay'] = (
    admission_dff['discharge_datetime'] - admission_dff['admit_datetime']
)


admission_dff = admission_dff.drop(columns=['admit_day', 'discharge_day'])
admission_dff = admission_dff.drop('admit_month', axis=1)
admission_dff['admit_month'] = admission_dff['admit_datetime'].dt.month
admission_dff['admit_day'] = admission_dff['admit_datetime'].dt.day_name
admission_dff = admission_dff.drop('admit_day', axis=1)
today = pd.Timestamp.today()


patient_df['age'] = (
    (today - patient_df['date_of_birth']).dt.days // 365
)
patient_df['age'].max()

patient_df['age'].min()
patient_df['age_group'] = pd.cut(
    patient_df['age'], bins = [0, 18, 35, 50, 65, 120],
    labels = [
    "0-18",
    "19-35",
    "36-50",
    '51-65',
    "65-120"
]
)

patient_df.head(10)
patient_df['age_group'].value_counts()
billing_df.head()
billing_df['patient_payment'].mean()
billing_df['admission_id'],(
    pa
)


billing_df.isnull().sum()
billing_df.duplicated()
departbed_df.isnull().sum()

#billing_df = pd.read_csv('billing(1).csv')
#departbed_df = pd.read_csv('department_beds.csv')
#dept = pd.read_csv('departments(1).csv')
#diagnose_df = pd.read_csv('diagnoses(1).csv')
#patient_df = pd.read_csv('patients(1).csv')
#treatment_df = pd.read_csv('treatment_events.csv')

adm_pat = admission_dff.merge(
    patient_df,
    on='patient_id',
    how='left'
)

adm_pat['admission_type'].value_counts()
adm_pat_dept = adm_pat.merge(
    dept,
    on= 'department_id',
    how='left'
)


adm_pat_dept = adm_pat_dept.merge(
    billing_df, 
    on='admission_id',
    how='left'
)

adm_pat_dept['payment_status'].value_counts()
diagnose_df.head()
hospital_db = adm_pat_dept.merge(
    diagnose_df, 
    on= 'diagnosis_code',
    how='left'

)
hospital_db.head(5)
treatment_df.head(3)
hospital_dbl = hospital_db.merge(
    treatment_df,
    on='admission_id',
    how='left'
)

hospital_dbl.head(5)
hospital_databasecsv = hospital_dbl.to_csv('hospital_database.csv', index=False)
admission_dff.groupby('admit_date')
['admission_id'].count()
hospital_dbd = pd.read_csv('hospital_database.csv')
hospital_dbd['length_of_stay'].describe()
hospital_dbd['length_of_stay'] = pd.to_numeric(hospital_dbd['length_of_stay'].str.replace('days', '', case=False),errors='coerce')
hospital_dbd['length_of_stay'].mean() 



###data exploratory analysis
hospital_dbd.groupby('dept_name_y')['length_of_stay'].mean().sort_values(ascending=False)

hospital_dbd['event_type']
hospital_dbd.groupby('diagnosis_name')['length_of_stay'].mean().sort_values(ascending=False).head(20)
hospital_dbd.groupby('event_type')['length_of_stay'].mean().sort_values(ascending=False).head(20)
hospital_dbd['outcome'].value_counts()
hospital_dbd['gender'].value_counts()

##visualization 

sns.set_theme(style = 'whitegrid')
gender_bar = hospital_dbd['gender'].value_counts().reset_index()
gender_bar.columns = ['gender', 'count']
sns.barplot( data = gender_bar, x = 'gender', y = 'count')
plt.show
hospital_dbd['age_group'].value_counts()
hospital_dbd.groupby('dept_name_x')['age'].mean().sort_values(ascending=False)
hospital_dbd['total_cost'].mean()
type(hospital_dbd['total_cost'])



hospital_dbd.groupby('dept_name_x')['total_cost'].mean().sort_values(ascending=False)
hospital_dbd.groupby('dept_name_x')['total_cost'].sum().sort_values(ascending=False)
hospital_dbd['payment_status'].value_counts()/100
hospital_dbd['diagnosis_name'].value_counts().head(20)
hospital_dbd.groupby('diagnosis_name')['total_cost'].mean().sort_values(ascending=False).head(20)
department_bed = pd.read_csv('department_beds.csv')
hospital_dbd['']

department_dbb.head(5)
labels = [' young_adult', 'adult', 'elderly', 'old', 'older' ]
data = hospital_dbd['age_group'].value_counts()
explode = [0.0, 0.0, 0.1, 0.0, 0.0]
plt.pie(data, labels=labels, explode=explode, autopct='%1.1f%%')
plt.show()
hospital_dbd['admission_type'].value_counts()




#exploratory data anaylsysis

pd.crosstab(
    hospital_dbd['admission_type'],
   hospital_dbd['outcome']
)
hospital_dbd.groupby(
    'admission_type'
)['length_of_stay'].mean()
hospital_dbd.groupby('dept_name_x').agg({
    'total_cost':'sum',
    'admission_id':'nunique'
})
hospital_dbd['insurance_ratio'] = (
    hospital_dbd['insurance_covered']
    /
  hospital_dbd['total_cost']
)
hospital_dbd.groupby(
    'age_group'
)['total_cost'].mean()

hospital_dbd.groupby(
    'diagnosis_name'
)['payment_status'].value_counts().head(20)
hospital_dbd.groupby(
    'age_group'
)['payment_status'].value_counts().head(20)
hospital_dbd['event_type'].value_counts()
hospital_dbd['event_hour'].value_counts()
hospital_dbd.groupby(
    'event_hour'
)['event_type'].value_counts().head(20)
hospital_dbd['staff_role'].value_counts()
pd.crosstab(
    hospital_dbd['staff_role'],
    hospital_dbd['event_type']
)
