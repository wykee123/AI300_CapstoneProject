# may24-team09
- Team Number & names of team members: may24-team09 - Kee Wee Yang, Tan Sing Yee
- Website URL of deployed Flask web application: http://ec2-52-77-224-76.ap-southeast-1.compute.amazonaws.com/ 
- Details on chosen final model and model parameters: 
    model: XGBClassifier
    parameters: objective='binary:logistic',  
                eval_metric='auc',
                tree_method='hist',        
                enable_categorical=True 
    hyperparameters:
    'colsample_bytree': 0.5, 'gamma': 0.9, 'max_depth': 3, 'reg_alpha': 0.9
    features:
    'tenure_months','total_monthly_fee','has_internet_service',
    'contract_type','num_referrals','num_dependents',
    'married','has_online_security','stream_movie',
    'stream_music','age'
- Offline AUC metric of chosen final model: 0.92

# TA Feedback
Amazing work on the capstone! Like the amount of details in model training. Here are some poitners
1. Do keep your commit messages consistent as a good practice. Just sharing an example for you to read up on if you are interested in the art of creating clear and concise git commit messages https://www.pullrequest.com/blog/mastering-the-art-of-git-commit-messages/
2. Use .env files to store sensitive credentials such as database connection details, especially when you publish your own public repository as there are malicious users who would misuse these credentials that you have published to the public and sometimes it might even cost you money

All in all execellent work on the capstone and congrats on completing AI300! Wishing you all the best :)
