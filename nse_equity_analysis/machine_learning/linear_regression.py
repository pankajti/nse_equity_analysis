from sklearn import  linear_model
reg=linear_model.LinearRegression()


def get_amount_ml(weight):
    weight_data = [[1], [2],[3]]
    price_data = [2, 4,7.5]
    reg.fit(weight_data, price_data)
    val = reg.predict(weight)
    return val




def get_amount(weight):
    return 2.5*weight


print(get_amount_ml(4))

print(get_amount_ml(54))


print(get_amount_ml(10098))
