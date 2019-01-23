window.onload=function(){
    setInterval(function(){
    var date=new Date();
    var h=date.getHours(); //获取小时
    var m=date.getMinutes(); //获取分钟
    var s=date.getSeconds(); //获取秒
    var d=document.getElementById('Date');
    if (h<=12) {
      var a='上午'
    }
    else {
      var a='下午'
    }
    if (h<10) {
      h = '0'+ h
    }
    if (m<10) {
      m = '0' + m
    }
    if (s<10) {
      s = '0' + s
    }
    d.innerHTML=a+' '+h+':'+m+':'+s;  },1000)
};
$(document).ready(function() {
    namespace = '/test_conn';
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
    //滚动条刷新到底
    var scroll_h = document.getElementById('log').scrollHeight;
    $('.messages').scrollTop(scroll_h);
　　　　　　　//连接后发送日志
    socket.on('connect', function(){
      console.log('connected')
    });
　　　　　　　//点击发送时将text框的内容发送到后端
    $('form#emit').submit(function(event) {
		var message_color = document.getElementById("ballid").style.background;
        socket.emit('imessage', {data: encodeURIComponent($('#emit_data').val().trim()), msg_color: message_color});
        $('#emit_data').val("");
        return false;
    });
　　　　　　  //接收后端广播的信息
    socket.on('message', function(msg) {
        var message = msg.data;
        var name = msg.username;
        var usernum = msg.usercount;
        var userall = msg.userall;
        var msg_box = msg.message_html;
        window.message = message;
        window.name = name;
        window.usernum = usernum;
        window.userall = userall;
        window.msg_box = msg_box;
		var message_color = document.getElementById("ballid").style.background;
		var font_color ="'" + "color" + ":" + message_color + ";" + "'";
		//console.log(msg_box.match("\"nick\""));
		msg_box = msg_box.replace(/\"nick\"/,font_color);
        $('#log').append("<br>" + msg_box);
        //$('#log').append('<br>'+ '<br>' + name + "(" + usernum + "/" + userall + ")" + ":" + $('<p/>').text(decodeURIComponent(message)).html());
        var scroll_h = document.getElementById('log').scrollHeight;
        $('.messages').scrollTop(scroll_h);
        //在线人数
        document.getElementById('Online').innerHTML = usernum + "/" + userall;
    });
});
window.onresize = function(){
        var h_st = window.outerHeight;
        if (document.hasFocus()) {
                var h_fn = window.outerHeight;
                //alert(h_st - h_fn);
                var sc_h = document.getElementById('log').scrollHeight;
                $('.messages').scrollTop(sc_h + h_st - h_fn);
        };
};