from sklearn.linear_model import LinearRegression
from height_app.models.user_model import get_users
import pandas as pd 

def msg_processor(msg_code):
    '''
    msg_processor returns a msg object with 'msg', 'type'
    where 'msg' corresponds to the message user sees
    and 'type' is the color of the alert element

    codes:
        - 0 : 필수값을 모두 채워주세요       - 1 : User does not exist
        - 2 : Unable to retrieve tweets
        - 3 : Successfully deleted user
    '''

    msg_code = int(msg_code)

    msg_list = [
        (
            'Successfully added to database',
            'success'
        ),
        (
            'User does not exist',
            'warning'
        ),
        (
            'Unable to retrieve tweets',
            'warning'
        ),
        (
            'Successfully deleted user',
            'info'
        ),
        (
            'Successfully updated to database',
            'success'
        ),
        (
            '필수 입력값을 모두 채워주세요',
            'warning'
        )
    ]

    return {
        'msg':msg_list[msg_code][0],
        'type':msg_list[msg_code][1]
    }

def predict_height(weight,father_height,mother_height):
    '''
    db로부터 데이터를 받아와서 키를 예측하는 함수입니다.
    '''

    user_list = get_users()
    data = {
        'ID':[user.id for user in user_list],
        'weight':[user.weight for user in user_list],
        'father_height':[user.father_height for user in user_list],
        'mother_height':[user.mother_height for user in user_list],
        'height':[user.height for user in user_list],
    }
    df = pd.DataFrame(data=data, columns=['ID','weight','father_height','mother_height','height'])

    X = df[["weight","father_height","mother_height"]]
    y = df['height']

    mlr = LinearRegression()
    mlr.fit(X,y)

    res_predicted = mlr.predict([[weight,father_height,mother_height]])
    return res_predicted
