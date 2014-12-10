/*This is the Ember application adapter.
Allow to configure the way Ember comunicates with the backend API
Endpoint paths can be prefixed with a namespace
*/
import DS from 'ember-data';  //Import the ember-data module

export default DS.RESTAdapter.extend({  //The RESTAdapter allows to comunicate with RESTs API's http://emberjs.com/guides/models/the-rest-adapter/
	namespace: '_ah/api/stockApi/v1'  	//Endpoint path customization
});
