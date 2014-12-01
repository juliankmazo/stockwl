import DS from 'ember-data';

export default DS.RESTAdapter.extend({
	namespace: '_ah/api/stockApi/v1'
});
