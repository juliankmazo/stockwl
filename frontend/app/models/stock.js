import DS from 'ember-data';

var Stock = DS.Model.extend({
  code: DS.attr('string'),
  companyName: DS.attr('string'),
  currentPrice: DS.attr('string'),
  pe: DS.attr('string'),
  priceSales: DS.attr('string'),
  eps: DS.attr('string'),
  totalCashPerShare: DS.attr('string'),
  bookValuePerShare: DS.attr('string'),
  dividendYield: DS.attr('string'),
  profitMargin: DS.attr('string'),
  totalDebt: DS.attr('string'),
  notes: DS.attr('string'),
  yearsDebt: DS.attr('string'),
  shares: DS.attr('string')
});

Stock.reopenClass({
  FIXTURES: [
    {id:1, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:2, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:3, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:4, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:5, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:6, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:7, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:8, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:9, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:10, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:11, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:12, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:13, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:14, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:15, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:16, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:17, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:18, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:19, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:20, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:21, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:22, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:23, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'}
  ]
});

export default Stock;