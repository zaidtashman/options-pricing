import quantsbin.derivativepricing as qbdp

"""### Defining Option Objects

In current release **Quantsbin** provide options to define under four asset classes.
Options on:
    1. Equity: qbdp.EqOption
    2. Futures: qbdp.FutOption
    3. Currencies: qbdp.FXOption
    4. Commodities: qbdp.ComOption
    
 Let's check doc string to get more information about Option objects.
"""

print(qbdp.EqOption.__doc__)

"""We can observe above that therevare five argumnents which are required for deifning an option.

Let's deifne our own Equity call option with European expiry.
"""

equity_option1 = qbdp.EqOption(option_type='Call', strike=57.5, expiry_date='20200320', expiry_type='European')

"""**Congrates!!!** you have defined you first option. Let's explore more into this option.

We will start with calculating payoff given Spot (current underlying price) is 55.
"""

print(equity_option1.payoff(58))

"""### Plotting Payoff

Let's plot the payoff profile for this option.

qbdp.Plotting takes first argument as option object, second argument as parameter to be plotted and this argument as range for which plot is required.

**Payoff Plotting**
"""

eq1_payoff = qbdp.Plotting(equity_option1,'payoff',x_axis_range=[45,70]).line_plot()
eq1_payoff.show()

"""### Option Pricing and Greeks Calculation

To price option we need two data points: Pricing Model and Market data.
We pass these two parameters to our option using engine method which returns engine object.

To start with we are using BlackScholesMerton as our pricing model and updating all other market parameters in engine.
"""

eq1_engine = equity_option1.engine(model='MC_GBM',pricing_date='20200211',spot0=53.8, rf_rate=0.0158, volatility=0.514)
eq1_engine = equity_option1.engine(model='BSM',pricing_date='20200212',spot0=55, rf_rate=0.0158, volatility=0.40)
print(eq1_engine.valuation()) #"""Calculating **Option Premium**"""

"""Calculating **Option Greeks**"""

print(eq1_engine.risk_parameters())

"""We can also check what all models are available for valuation by using below command"""

print(equity_option1.list_models())

"""Once we have engine object ready, we can start by plotting pnl profile.
PnL is simply payoff minus current option premium

Note: We need to pass pricing object for pnl plot, unlike payoff plot where we pass option object

**PnL Plotting**
"""

eq1_pnl = qbdp.Plotting(eq1_engine, 'pnl', x_axis_range=[50,60]).line_plot()
eq1_pnl.show()

"""** Plotting Premium and Payoff together **"""

eq1_payoff = qbdp.Plotting(equity_option1,'payoff',x_axis_range=[50,60]).line_plot()
eq1_pnl = qbdp.Plotting(eq1_engine, 'valuation', x_axis_range=[50,60]).line_plot()
eq1_pnl.show()

"""** Plotting Greeks **

**Delta**
"""

eq1_delta = qbdp.Plotting(eq1_engine, 'delta', x_axis_range=[50,60]).line_plot()
eq1_delta.show()

"""**Gamma**"""

eq1_gamma = qbdp.Plotting(eq1_engine, 'gamma', x_axis_range=[50,60]).line_plot()
eq1_gamma.show()

"""**Theta**"""

eq1_theta = qbdp.Plotting(eq1_engine, 'theta', x_axis_range=[50,60]).line_plot()
eq1_theta.show()

"""**Vega**"""

eq1_vega = qbdp.Plotting(eq1_engine, 'vega', x_axis_range=[50,60]).line_plot()
eq1_vega.show()

"""**Rho**"""

eq1_rho = qbdp.Plotting(eq1_engine, 'rho', x_axis_range=[50,60]).line_plot()
eq1_rho.show()

"""** In next tutorial we will further deep dive into valuation of options on different asset classes
and available market parameters to tweek**
"""