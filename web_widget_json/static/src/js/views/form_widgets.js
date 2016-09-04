odoo.define("web_widget_json.form_widgets", function (require) {
    "use strict";

    var core = require('web.core');
    var form_widgets = require('web.form_widgets');
    var formats = require('web.formats');
    var dom_utils = require('web.dom_utils');

    var FieldJson = form_widgets.FieldChar.extend({
        render_value: function() {
            if (this.get("effective_readonly")) {
                var txt = JSON.stringify(this.get("value") || '{}');
                this.$el.text(txt);
            } else {
                var show_value = formats.format_value(
                    this.get('value'), this, '{}'
                );
                this.$el.val(JSON.stringify(show_value));
                dom_utils.autoresize(this.$el, {parent: this});
            }
        },
    });

    core.form_widget_registry.add('json', FieldJson);

    return FieldJson;
});
