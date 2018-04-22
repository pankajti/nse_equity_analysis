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


def get_amount_ml2(weight):
    weight_data = [[1,1.5], [2,1.5]]
    price_data = [3.5, 5.5, ]
    reg.fit(weight_data, price_data)
    val = reg.predict([[weight],[1.5]])
    return val


def get_amount2(weight):
    price=2*weight
    spenditure=1.5
    return price +spenditure



print(get_amount2(4))

print(get_amount2(54))


print(get_amount2(10098))




print(get_amount_ml2(4))

#print(get_amount_ml2([54,1.5]))


#print(get_amount_ml2([10098,1.5]))
