let breadcrumb = '<ul class="bread-crumb px-0">\n' +
    '  <li><a href="/"><span class="fa fa-home"> </span> Trang chủ</a></li>\n' +
    '  <li><a href="/course">Khóa học</a></li>\n' +
    '  <li><a href="/contact">INT3306 4</a></li>\n' +
    '  </ul>';

Vue.component('breadcrumb', {template: breadcrumb });

new Vue({
    el: '#inner-course-body',
})