/*
This allows to adapt the payload returned from the server responses.
*/
import DS from 'ember-data';  //Import ember data module
import Ember from 'ember';  //Import ember app

export default DS.RESTSerializer.extend({ // REST serialazer module

	serializeIntoHash: function(hash, type, record, options) { //This function fix the way ember send data to the server
		Ember.merge(hash, this.serialize(record, options)); //More info in https://github.com/emberjs/data/issues/771
	},

	extractMeta: function(store, type, payload) {  // Extract data from the responses in order to parse metadata as records
    if (payload && payload.kind) {
      delete payload.kind;  // keeps ember data from trying to parse "kind" as a record
    }
    if (payload && payload.etag) {
      delete payload.etag;  // keeps ember data from trying to parse "etag" as a record
    }

    if (!payload.stocks) {  // If there is no stocks in the ndb
      payload.stocks=[];  // set the response as an empty array to prevent an error from ember
    } 
  }
});
