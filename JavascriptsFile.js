//Starting from scratch
function answerA(){
	if (document.getElementById("a").innerHTML=="start")
	{
		document.getElementById("story").innerHTML="You wake up on an isolated island,alone.\nYou look to your sidesand all you see is a machete,small axe and a few coconut trees.";
		document.getElementById("Q").innerHTML="What is the first thing you do?";
		document.getElementById("a").innerHTML="try to climb a tree and get coconuts";
		document.getElementById("b").innerHTML="chop down a tree";
		document.getElementById("c").innerHTML="search around the island";
	}
//trying to be a monkey
else if (document.getElementById("a").innerHTML=="try to climb a tree and get coconuts")
	{
		document.getElementById("story").innerHTML="you start climbing the tree and find out its a lot harder than the moviesmake it look like and fall back down to the ground mid climb'\neven with that your fine... for now";
		document.getElementById("Q").innerHTML="will you keep trying?";
		document.getElementById("a").innerHTML="Yes, of course(stubbornly)";
		document.getElementById("b").innerHTML="No, i'll leave it to the monkeys...";
		document.getElementById("c").innerHTML="0";
	}
//that was quick
else if (document.getElementById("a").innerHTML=="Yes, of course(stubbornly)")
	{
		document.getElementById("story").innerHTML="you give it another try and it isn't any  easier than it was the first time.\nwith the experienc you gaind from the first try you manage to almost get to the top but then a coconut falls on you and then to the ground,\nshattering into many small shards and knocking you down in the prosses, you fall on the small shards and bleed out...";
		document.getElementById("Q").innerHTML="THE END";
		document.getElementById("a").innerHTML="ouch";
		document.getElementById("b").innerHTML="ouch";
		document.getElementById("c").innerHTML="ouch";
	}
//one gone, only... to go
else if (document.getElementById("a").innerHTML=="create a fireplace and burn it all duhh!!")
	{
		document.getElementById("story").innerHTML="you make a fireplace and use some wood to keep it lit up through the night, other then homeless your'e totaly fine.\nyou wake up nad see you have a bunch of leftover wood and a few coconuts.\nyou think to yourself'maybe i should fine civilisation'";
		document.getElementById("Q").innerHTML="what are you gonna use the leftover wood for?";
		document.getElementById("a").innerHTML="build a raft, Dora the explorer style";
		document.getElementById("b").innerHTML="try to build a huge burning SOS sign";
		document.getElementById("c").innerHTML="i didn't think that!!!, ill build a shelter at last!";
	}
//time to go!
else if (document.getElementById("a").innerHTML=="build a raft, Dora the explorer style")
	{
		document.getElementById("story").innerHTML="you make a scrappy raft that barly float with you on it, you decide to use a yleftover plank as a paddle.\nnow you just need to pick where to go...yeah...just a random direction i guess...";
		document.getElementById("Q").innerHTML="to which direction will you go to?";
		document.getElementById("a").innerHTML="one direction";
		document.getElementById("b").innerHTML="the other direction";
		document.getElementById("c").innerHTML="0";
	}
//deepsea encounter1
else if (document.getElementById("a").innerHTML=="")
	{
		document.getElementById("story").innerHTML="";
		document.getElementById("Q").innerHTML="";
		document.getElementById("a").innerHTML="";
		document.getElementById("b").innerHTML="";
		document.getElementById("c").innerHTML="";
	}





















}