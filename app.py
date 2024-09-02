
import joblib
import gradio as gr
import numpy as np
import os

script_dir = os.path.dirname(__file__)  


model_filename = 'models/LightGBM_model.pkl'
model_path = os.path.join(script_dir, model_filename)


model = joblib.load(model_path)


loanStatusMapping = {0 : 'CSR Voided New Loan', 1 : 'Charged Off', 2 : 'Charged Off Paid Off', 3 : 'External Collection', 4 : 'Internal Collection', 5 : 'New Loan',6 : 'Paid Off Loan',7 : 'Pending Paid Off',8 : 'Rejected', 9 : 'Returned Item', 10 : 'Settled Bankruptcy', 11 : 'Settlement Paid Off', 12 : 'Settlement Pending Paid Off', 13 : 'Withdrawn Application'}
 

def predictloanStatus(loan_amount, apr, pay_frequency, lead_type, lead_cost, fp_status, has_cf):
    
    input_data = np.array([[loan_amount, apr, pay_frequency, lead_type, lead_cost, fp_status, has_cf]])
    
  
    prediction = model.predict(input_data)[0]
    
   
    prediction_text = loanStatusMapping[prediction]
    
    return prediction_text


iface = gr.Interface(
    fn=predictloanStatus,
    inputs=[
        gr.Number(label="Loan Amount"),
        gr.Number(label="APR"),
        gr.Number(label="Pay Frequency (B: 0, I: 1, M: 2, S: 3, W: 4)"),  
        gr.Number(label="Lead Type (bvMandatory: 0, California: 1, Express: 2, Instant-offer: 3, Lead: 4, Lionpay: 5, Organic: 6, Prescreen: 7, Rc_returning: 8, Repeat: 9)"),      
        gr.Number(label="Lead Cost"),
        gr.Number(label="FP Status (Cancelled: 0, Checked: 1, No Payments: 2, Pending: 3, Rejected: 4, Returned: 5, Skipped: 6)"),      
        gr.Number(label="Has CF ")         
    ],
    outputs=gr.Textbox(label="Loan Status Prediction"),
    title="Loan Status Prediction",
    description="Enter the loan details to predict the loan status."
)


if __name__ == '__main__':
    iface.launch(share=True, server_name="127.0.0.1", server_port=7861)
