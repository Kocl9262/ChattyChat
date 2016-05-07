function insertSmiley(smiley)
    {
    
        var currentText = document.getElementById("emote");
        
        var smileyWithPadding = smiley;
        currentText.value += smileyWithPadding;
    currentText.focus();
    
    }
