/*jslint browser: true*/
/*global $, jQuery, alert*/

//表格操作栏配置
var operatorObj = {
	operateFormatter: function (value, row, index) { //初始操作栏的按钮
		'use strict';
		return ['<a class="write" href="javascript:void(0)" title="查看详情" style="margin:0">',
                '<i class="glyphicon glyphicon-eye-open"></i>查看详情',
                '</a>'
            ].join(''); //配置表格操作栏的内容
	},
	operateEvents: { //点击时触发的事件
		'click .write': function (e, value, row, index) {
			'use strict';
			alert(row.name);
		}
	}
};


function getValue(value, row, index) {
	'use strict';
	if (value >= 18) {
		return "<span>已成年</span>";
	} else {
		return "<span>未成年</span>";
	}
}

$('#table').bootstrapTable({
	url: '../static/js/data1.json',
	columns: [{
		field: 'statebox',
		checkbox: true
	}, {
		field: 'name',
		title: '订阅名称'
		//		class: 'red'
	}, {
		field: 'age',
		title: '订阅地址',
		sortable: true,
		formatter: function (value, row, index) {
			'use strict';
			return getValue(value);
		}
	}, {
		field: 'id',
		title: '证件号'
	}, {
		width: "150px",
		field: 'operate',
		title: '相关操作',
		align: 'center',
		events: operatorObj.operateEvents,
		formatter: operatorObj.operateFormatter
	}],
	undefinedText: '没有数据',
	striped: true, //各行效果
	sortName: 'age',
	sortOrder: 'desc',
	pagination: true,
	pageSize: 5,
	pageNumber: 1,
	paginationPreText: '<--',
	paginationNextText: '-->',
	paginationHAlign: 'right',
	search: true,
	searchOnEnterKey: true,
	searchText: '',
	strictSearch: false,
	showHeader: true,
	showFooter: true,
	showRefresh: true,
	cardView: false,
	showToggle: true,
	showColumns: true,
	minimumCountColumns: 5,
	detailView: true,
	detailFormatter: function (index, row) { //index:行号，row：行数据
		'use strict';
		var htm, len;
		len = index + 1;
		htm = len + '<br/>' + '姓名：' + row.name + '<br/>' + '年龄：' + row.age + '<br/>' + '证件号：' + row.id;
		return htm; //返回视图
	},
	clickToSelect: true,
	singleSelect: false,
	rowStyle: function (row, index) {
		'use strict';
		return {
			css: {
				"color": "blue"
			}
		};
	},
	toolbar: '#toolbar', //制定哪个容器做工具栏
	searchAlign: 'right',
	buttonsAlign: 'right',
	toolbarAlign: 'left',
	//	toolbarAlign: 'left',
	//	onClickRow: function (row, $element, field) {
	//		'use strict';
	//		var i = $element.data('index'); //可通过此参数获取当前行号
	//		alert(i + "，" + row.age + "，" + field);
	//	}
	//	onClickCell: function (field, value, row, $element) {
	//		'use strict';
	//		alert(field + "，" + value + "，" + row.id); //value当前点击列所在行的内容，可以直接理解为单元格的内容，row为当前点击列所在行的所有数据
	//	}
	onSort: function (name, order) {
		'use strict';
		if (order === "asc") {
			order = "升序排列";
		} else {
			order = "降序排列";
		}
		alert(name + order);
	},
	onCheck: function (row) {
		'use strict';
		alert("您选中的行的name为" + row.name + "，您选中的行的age为" + row.age + "，您选中的行的id为" + row.id);
	}

});





//$('#table').on("click-row.bs.table", function (e, row, $element, field) {
//	'use strict';
//	var i = $element.data('index'); //可通过此参数获取当前行
//	alert(i + "，" + row.age + "，" + field);
//});
