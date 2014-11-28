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
    {id:2, code:'ELX', companyName: 'Ellex Medical Lasers Limited', currentPrice:'$0.29', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:3, code:'CIR', companyName: 'Circadian Technologies Limited', currentPrice:'$0.17', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:4, code:'MGX', companyName: 'Mount Gibson Iron Limited', currentPrice:'$0.41', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:5, code:'ACR', companyName: 'Acrux Limited', currentPrice:'$1.28', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:6, code:'CMG', companyName: 'Chandler Macleod Group Limited', currentPrice:'$0.34', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:7, code:'BLY', companyName: 'Boart Longyear Ltd.', currentPrice:'$0.19', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:8, code:'OSL', companyName: 'Oncosil Medical Ltd', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:9, code:'RNO', companyName: 'Rhinomed Ltd', currentPrice:'$0.03', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:10, code:'XRF', companyName: 'XRF Scientific Limited', currentPrice:'$0.18', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:11, code:'FRI', companyName: 'Finbar Group Limited', currentPrice:'$1.39', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:12, code:'IRI', companyName: 'Integrated Research Limited', currentPrice:'$0.98', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:13, code:'CDD', companyName: 'Cardno Limited', currentPrice:'$3.22', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:14, code:'FPS', companyName: 'Fiducian Portfolio Services Limited', currentPrice:'$1.62', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:15, code:'MLB', companyName: 'Melbourne IT Limited', currentPrice:'$1.32', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:16, code:'MFC', companyName: 'Metals Finance Ltd', currentPrice:'$0.07', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:17, code:'LCT', companyName: 'Living Cell Technologies Ltd.', currentPrice:'$0.08', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:18, code:'RFL', companyName: 'Rubik Financial Limited', currentPrice:'$0.25', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:19, code:'CGO', companyName: 'CPT Global Limited', currentPrice:'$0.69', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:20, code:'AAX', companyName: 'Ausenco Limited', currentPrice:'$0.46', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:21, code:'ATP', companyName: 'Atlas Pearls and Perfumes Ltd', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:22, code:'TFC', companyName: 'TFS Corporation Limited', currentPrice:'$1.26', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'},
    {id:23, code:'ACG', companyName: 'Atcor Medical Holdings', currentPrice:'$0.09', pe:'N/A', priceSales:'2.93', eps:'-$0.02', totalCashPerShare:'$0.01', bookValuePerShare:'$0.02', dividendYield:'0.00%', profitMargin:'-52.71%', totalDebt:'$0.00', notes:'buy', yearsDebt:'0.00', shares:'157,440,325'}
  ]
});

export default Stock;