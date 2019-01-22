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
　　　　　　　//连接后发送日志
    socket.on('connect', function(){
      console.log('connected')
    });
　　　　　　　//点击发送时将text框的内容发送到后端
    $('form#emit').submit(function(event) {
        socket.emit('imessage', {data: encodeURIComponent($('#emit_data').val().trim())});
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
        $('#log').append("<br>" + msg_box);
    });
        //在线人数统计
    socket.on('user count', function(usr) {
        $('#Date').html(usr.count);
    });
    $('#btn1').click(function() {
        //$('#log').append('<br>'+ '<br>' + name + "(" + usernum + "/" + userall + ")" + ":" + $('<p/>').text(decodeURIComponent(message)).html());
        var scroll_h = document.getElementById('log').scrollHeight;
        $('.messages').scrollTop(scroll_h);
    });
});
