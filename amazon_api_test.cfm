<!--- Just a proof of concept for an older version of Grapevinyl --->

<cfif isdefined("form.artist") and isdefined("form.album") and trim(form.artist) NEQ "" and trim(form.album) NEQ "">

  <cfset amazonKey = "your_key_here">
	<cfset artistURI = URLEncodedFormat(form.artist)>
	<cfset albumURI = URLEncodedFormat(form.album)>

	<cfoutput>
	<form name="driver" action="#CGI.SCRIPT_NAME#" method="post">
		artist<br>
		<input name="artist" type="text" value="#form.artist#"><br/><br/>
		album<br>
		<input name="album" type="text" value="#form.album#"><br/><br/>
		perceived rating<br/>
		<select name="rating">
			<cfif form.rating IS 1><option value="1" selected>1 - sucks</option><cfelse><option value="1">1 - sucks</option></cfif>
			<cfif form.rating IS 2><option value="2" selected>2</option><cfelse><option value="2">2</option></cfif>
			<cfif form.rating IS 3><option value="3" selected>3</option><cfelse><option value="3">3</option></cfif>
			<cfif form.rating IS 4><option value="4" selected>4</option><cfelse><option value="4">4</option></cfif>
			<cfif form.rating IS 5><option value="5" selected>5 - love it</option><cfelse><option value="5">5 - love it</option></cfif>
		</select><br><br/>
		tags (separated by spaces)<br>
		<input type="text" name="tags" size="60" value="#form.tags#"><br/><br/>
		<input type="submit" value="get album art">
	</form>
	</cfoutput>

	<cfhttp
		method="get"
		url="http://webservices.amazon.com/onca/xml?Service=AWSECommerceService&SubscriptionId=#amazonKey#&Operation=ItemSearch&SearchIndex=Music&Artist=#artistURI#&Title=#albumURI#&ResponseGroup=Medium,Images"></cfhttp>
	
	<cfset document = #XMLParse(cfhttp.FileContent)#>
	
	<cfif NOT isdefined("document.XMLRoot.Items.Request.Errors.Error.Message.XMLText")>
	
		<cfset itemroot = document.XMLRoot.Items.Item>
		
		<cfset detailpageurl = itemroot.DetailPageURL.XMLText>
		<cfif isdefined("itemroot.LargeImage")>
			<cfset imgurl = itemroot.LargeImage.URL.XMLText>
			<cfset imgheight = itemroot.LargeImage.Height.XMLText>
			<cfset imgwidth = itemroot.LargeImage.Width.XMLText>
		</cfif>
		<cfset amazonartist = itemroot.ItemAttributes.Artist.XMLText>
		<cfset amazonalbum = itemroot.ItemAttributes.Title.XMLText>
		<cfset amazonreleasedate = itemroot.ItemAttributes.ReleaseDate.XMLText>
		<cfset amazonlabel = itemroot.ItemAttributes.Label.XMLText>
		
		<cfoutput>
		<h2>#amazonartist#</h2>
		<h3>#amazonalbum# (#left(amazonreleasedate,4)#)</h3>
		<cfif isdefined("imgurl")>
			<a href="#detailpageurl#"><img src="#imgurl#" width="#imgwidth#" height="#imgheight#" border="0"></a><br>
		<cfelse>
			could not find cover art for you. don't worry - you can try updating this any time in the future.
		</cfif>
		</cfoutput>
		
	<cfelse>
		
		could not find cover art for you. don't worry - you can try updating this any time in the future.
		
	</cfif>

<cfelse>

	<cfoutput>
	<form name="driver" action="#CGI.SCRIPT_NAME#" method="post">
		artist<br>
		<input name="artist" type="text"><br/><br/>
		album<br>
		<input name="album" type="text"><br/><br/>
		perceived rating<br/>
		<select name="rating">
			<option value="1">1 - sucks</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5 - love it</option>
		</select><br><br/>
		tags (separated by spaces)<br>
		<input type="text" name="tags" size="60"><br/><br/>
		<input type="submit" value="get album art">
	</form>
	</cfoutput>

</cfif>