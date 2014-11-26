import DS from 'ember-data';

export default DS.Model.extend({
  code: DS.attr('string'),
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
