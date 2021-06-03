# constructing a Backtesting function

def backtesting(dataframe):
    # We will first need to extract out the index of each Buy & Sell price 
    # This is needed to get the 'Opening Price' of the next day - when the actual trade takes place
    Buy = []
    Sell = []
    
    for i in range(len(dataframe['Buy_Signal_Price'])):
               if not np.isnan(dataframe['Buy_Signal_Price'][i]):
                   Buy.append(i)
                    
    for i in range(len(dataframe['Sell_Signal_Price'])):
               if not np.isnan(dataframe['Sell_Signal_Price'][i]):
                   Sell.append(i)
                                
    Realbuys = [i+1 for i in Buy] 
    Realsells = [i+1 for i in Sell]
    
    # We extract out the opening price for the day after the respective signals
    Buyprices = dataframe.Open.iloc[Realbuys]
    Sellprices = dataframe.Open.iloc[Realsells]
    
    # We will be dropping the signals if the selling signal is preceeded with no buying signal
    # Also applies for the signals if the buying signal is followed with no selling signal
    if Sellprices.index[0] < Buyprices.index[0]:
        Sellprices = Sellprices.drop(Sellprices.index[0])
    elif Buyprices.index[-1] > Sellprices.index[-1]:
        Buyprices = Buyprices.drop(Buyprices.index[-1])
        
    # we would now be calculating relative profits 
    relative_profits = []
    for i in range(len(Sellprices)):
        relative_profits.append((Sellprices[i] - Buyprices[i])/Buyprices[i])
        return sum(relative_profits)/len(relative_profits) * 100