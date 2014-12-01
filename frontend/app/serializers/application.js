import DS from 'ember-data';
import Ember from 'ember';

export default DS.RESTSerializer.extend({

	serializeIntoHash: function(hash, type, record, options) {
		Ember.merge(hash, this.serialize(record, options));
	},

	extractMeta: function(store, type, payload) {
    if (payload && payload.kind) {
      // store.metaForType(type, { total: payload.kind });  // sets the metadata for "post"
      delete payload.kind;  // keeps ember data from trying to parse "total" as a record
    }
    if (payload && payload.etag) {
      // store.metaForType(type, { total: payload.etag });  // sets the metadata for "post"
      delete payload.etag;  // keeps ember data from trying to parse "total" as a record
    }

    if (!payload.stocks) {
      payload.stocks=[];
    }
  }
});
