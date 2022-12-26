document.getElementById("#odemebuton").onclick = function(){
    document.getElementById("#odemebuton").innerHTML ="✅ Ödemeye Geçiliyor..."
    document.getElementById("#odemebuton").style.fontSize = "15px"
    document.getElementById("#odemebuton").style.transition= "1s";
    document.getElementById("#odemebuton").style.color= "white";
    document.getElementById("#odemebuton").style.background= "none";
    document.getElementById("urun15").style.display = "none"
    document.getElementById("urun6").style.display = "none"
    document.getElementById("urun5").style.display = "none"
    document.getElementById("odemeyazi").innerHTML= "BİZİ SEÇTİĞİNİZ İÇİN TEŞEKKÜR EDERİZ. ❤️" 
  }
  document.getElementById("sil1").onclick = function(){
    document.getElementById("urun5").style.display = "none"
  }
  document.getElementById("sil2").onclick = function(){
    document.getElementById("urun6").style.display = "none"
  }
  document.getElementById("sil3").onclick = function(){
    document.getElementById("urun15").style.display = "none"
  }
  deger=23999
  document.getElementById("samsunspor").onclick = function(){
    document.getElementById("sagt").value = deger+document.getElementById("sagt").value++;
    document.getElementById("adet1").value ++;
     if (document.getElementById("adet1").value == 11){
      document.getElementById("yanyazi").innerHTML = "Sepete En Fazla 10 Ürün Ekleyebilirsiniz."
      document.getElementById("adet1").value = 10
      document.getElementById("sagt").value = 239990
      
    }
  }

  document.getElementById("button2azalt").onclick = function(){
    document.getElementById("sagt").value -= deger;
    document.getElementById("adet1").value --;
    if (document.getElementById("adet1").value == -1){
      document.getElementById("adet1").value = 0
      document.getElementById("sagt").value = 0
    }
  }
  document.getElementById("buton2").onclick = function(){
    document.getElementById("sagt2").value = deger+document.getElementById("sagt2").value++;
    document.getElementById("adet11").value ++;
     if (document.getElementById("adet11").value == 11){
      document.getElementById("yanyazi2").innerHTML = "Sepete En Fazla 10 Ürün Ekleyebilirsiniz."
      document.getElementById("adet11").value = 10
      document.getElementById("sagt2").value = 239990
      
    }
  }
  document.getElementById("buton3").onclick = function(){
    document.getElementById("sagt2").value -= deger;
    document.getElementById("adet11").value --;
    if (document.getElementById("adet11").value == -1){
      document.getElementById("adet11").value = 0
      document.getElementById("sagt2").value = 0
    }
  }
  document.getElementById("buton4").onclick = function(){
    document.getElementById("sagt3").value = deger+document.getElementById("sagt3").value++;
    document.getElementById("adet3").value ++;
     if (document.getElementById("adet3").value == 11){
      document.getElementById("yanyazi3").innerHTML = "Sepete En Fazla 10 Ürün Ekleyebilirsiniz."
      document.getElementById("adet3").value = 10
      document.getElementById("sagt3").value = 239990
      
    }
  }
  document.getElementById("buton5").onclick = function(){
    document.getElementById("sagt3").value -= deger;
    document.getElementById("adet3").value --;
    if (document.getElementById("adet3").value == -1){
      document.getElementById("adet3").value = 0
      document.getElementById("sagt3").value = 0
    }
  }