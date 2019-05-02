var DatatableJsonRemoteDemo = {
    init: function () {
        var t, e;
        t = $(".m_datatable").mDatatable({
            data: {
                type: "remote",
                source: "exercise-data.json",
                pageSize: 10
            },
            layout: {theme: "default", class: "", scroll: !1, footer: !1},
            sortable: !0,
            pagination: !0,
            search: {input: $("#generalSearch")},
            columns: [
                {field: "job_history", title: "Job History"},
                {field: "company", title: "Company"},
                {field: "email", title: "Email"},
                {field: "city", title: "City"},
                {field: "name", title: "Name"},
                {field: "country", title: "Country"}]
        }), e = t.getDataSourceQuery(), $("#m_form_status").on("change", function () {
            t.search($(this).val(), "Status")
        }).val(void 0 !== e.Status ? e.Status : ""), $("#m_form_type").on("change", function () {
            t.search($(this).val(), "Type")
        }).val(void 0 !== e.Type ? e.Type : ""), $("#m_form_status, #m_form_type").selectpicker()
    }
};
jQuery(document).ready(function () {
    DatatableJsonRemoteDemo.init()
});