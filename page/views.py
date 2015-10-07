from django.shortcuts import render


from datetime import datetime
from django.http import HttpResponse


def hello_world(request):
    output = """
<!DOCTYPE html>
<!-- saved from url=(0030)http://programmingexcuses.com/ -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
 <title>Excuses For Lazy Coders</title>
<!--  <meta name="keywords" content="Programming, Programmer, Devloping, Developer, Coding, Coders, Excuses, Reasons, Lies, Fibs, Blame, Justifications">
 <meta name="description" content="Excuses For Lazy Coders"> -->
 <link rel="canonical" href="./Excuses For Lazy Coders_files/Excuses For Lazy Coders.html">
 <style type="text/css">* {margin: 0;} html, body {height: 100%;} .wrapper {min-height: 100%; height: auto !important; height: 100%; margin: 0 auto -8em;} .footer, .push {height: 8em;}</style>
</head>
<body data-feedly-mini="yes">
 <div class="wrapper">
  <center style="color: #333; padding-top: 200px; font-family: Courier; font-size: 24px; font-weight: bold;"><a href="./Excuses For Lazy Coders_files/Excuses For Lazy Coders.html" rel="nofollow" style="text-decoration: none; color: #333;">That code was written by the last guy</a></center>
  <div class="push"></div>
 </div>
 <div class="footer">
  <center style="color: #333; font-family: Courier; font-size: 11px;">
   // <script type="text/javascript" async="" src="./Excuses For Lazy Coders_files/ga.js"></script><script async="" type="text/javascript" src="./Excuses For Lazy Coders_files/ca-pub-4336860580083128.js"></script><script type="text/javascript"><!--
   //  google_ad_client = "ca-pub-4336860580083128";
   //  google_ad_slot = "1671975908";
   //  google_ad_width = 728;
   //  google_ad_height = 90;
   //  //-->
   // </script>
   <script type="text/javascript" src="./Excuses For Lazy Coders_files/show_ads.js"></script><ins id="aswift_0_expand" style="display:inline-table;border:none;height:90px;margin:0;padding:0;position:relative;visibility:visible;width:728px;background-color:transparent"><ins id="aswift_0_anchor" style="display:block;border:none;height:90px;margin:0;padding:0;position:relative;visibility:visible;width:728px;background-color:transparent"><iframe width="728" height="90" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_0" name="aswift_0" style="left:0;position:absolute;top:0;"></iframe></ins></ins>
   <br><br>© Copyright 2012 - 2015 programmingexcuses.com - All Rights Reserved
  </center>
 </div>
 // <script type="text/javascript">
 //  var _gaq = _gaq || [];
 //  _gaq.push(['_setAccount', 'UA-33167244-1']);
 //  _gaq.push(['_setDomainName', 'programmingexcuses.com']);
 //  _gaq.push(['_setAllowLinker', true]);
 //  _gaq.push(['_trackPageview']);
 //  (function() {
 //   var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 //   ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 //   var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
 //  })();
 // </script>

<div id="feedly-mini" title="feedly Mini tookit"></div></body></html>
    """.format(current_time=datetime.now())

    return HttpResponse(output)

# Create your views here.
