<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<title>products to popular tags</title>
<style type="text/css">
<!--
body {width: 700px;	font: normal 12px Arial, Helvetica, sans-serif; line-height: 30px;}
.productTag:link { margin-bottom: 10px; text-decoration: none; padding-bottom: 2px;	}
.productTag:visited { color: #0063DC; text-decoration: none; }
.productTag:hover { color: #ffffff; text-decoration: none; background: #0063DC;	}
.productTag:active { color: #ffffff; text-decoration: none; background: #FF0084; }
-->
</style>
</head>

<body>

<!--- Determine the total number of rows and tiers --->
<cfset total_rows = 100>
<cfset total_tiers = 5>
<cfset rows_per_tier = total_rows/total_tiers>

<!--- First get all the best 50 products --->
<cfquery name="getProducts_count" datasource="exp" maxrows="#total_rows#">
select productName, productCount
from product1
order by productCount desc;
</cfquery>

<!---<cfdump var="#getProducts_count#">--->

<!---
<!--- Make a 2-dimensional array to figure out what range each product is within --->
<cfset productsArray = ArrayNew(2)>

<!--- Do a nested loop to store the data in the array --->
<cfset tempstart = 1>
<cfset tempend = rows_per_tier>
<cfloop index="currentTier" from="#total_tiers#" to="1" step="-1" >
	<cfset cheapcounter = 1>
	<cfoutput>processing tier: #currentTier#<br></cfoutput>
	<cfloop query="getProducts_count" startrow="#tempstart#" endrow="#tempend#">
		<cfoutput>#productName#</cfoutput>
		<cfoutput><cfset productsArray[#currentTier#][#cheapcounter#] = #productName#></cfoutput>
		<cfset cheapcounter = cheapcounter + 1>
	</cfloop>
	<br><br>
	<cfset tempstart = tempend + 1>
	<cfset tempend = tempend + rows_per_tier>
</cfloop>

<cfdump var="#productsarray#">
--->


<!--- could i simply append a new column to the query??? --->
<cfset singleArray = ArrayNew(1)>
<cfset newstart = 1>
<cfset newend = rows_per_tier>
	<cfset cc = 1>
<cfloop index="myTier" from="#total_tiers#" to="1" step="-1">
	<cfloop query="getProducts_count" startrow="#newstart#" endrow="#newend#">
		<cfoutput><cfset singleArray[#cc#] = #myTier#></cfoutput>
		<cfset cc = cc + 1>
	</cfloop>
</cfloop>
<cfset newcol = QueryAddColumn(getProducts_count,"tier",singlearray)>
<!---<br><br><cfdump var="#getProducts_count#"><br><br>--->

<!--- Now go and order the query by the name --->
<cfquery name="getProducts_alpha" dbtype="query" maxrows="#total_rows#">
select *
from getProducts_count
order by productName asc;
</cfquery>

<!--- Now output the data set --->
<h1>my favorite things</h1>
<p>here are the top <cfoutput>#total_rows#</cfoutput> products. the bigger the link, the more popular they are.</p>
<p style="padding: 20px 30px 20px 20px; border: solid 1px #eee; background: #f5f5f5;">
<cfoutput query="getProducts_alpha" maxrows="#total_rows#">
	<cfswitch expression="#tier#">
		<cfcase value="5"><a href="##" class="productTag" style="font-size: 28px;">#lcase(productname)#</a></cfcase>
		<cfcase value="4"><a href="##" class="productTag" style="font-size: 22px;">#lcase(productname)#</a></cfcase>
		<cfcase value="3"><a href="##" class="productTag" style="font-size: 18px;">#lcase(productname)#</a></cfcase>
		<cfcase value="2"><a href="##" class="productTag" style="font-size: 14px;">#lcase(productname)#</a></cfcase>
		<cfcase value="1"><a href="##" class="productTag" style="font-size: 11px;">#lcase(productname)#</a></cfcase>
	</cfswitch>
	&nbsp;&nbsp;
</cfoutput>
</p>

<cfquery name="total_records" datasource="exp">
select *
from product1
</cfquery>

<p>note, this is just a sample. there are <cfoutput>#total_records.recordcount#</cfoutput> in the database.</p>

</body>
</html>