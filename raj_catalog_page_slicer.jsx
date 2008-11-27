// A quick proof of concept to automate site thumbnails

total_pages = 44;
catalog_season = "fall_2008";

full_document_path = "~/Documents/Repositories/decorbyraj.com/Assets/" + catalog_season + "/catalog_with_prices.pdf";
full_output_path = "~/Documents/Repositories/decorbyraj.com/Assets/" + catalog_season + "/jpg/with_prices/full/";
thumbs_output_path = "~/Documents/Repositories/decorbyraj.com/Assets/" + catalog_season + "/jpg/with_prices/thumbs/";

function open_document(page, type)
{
    FileReference = new File(full_document_path);
    PDFOpenOptions = new PDFOpenOptions();  
    PDFOpenOptions.page = page;
    PDFOpenOptions.resolution = 72;
    //if (type == "thumb")
    //{
    //	PDFOpenOptions.width = 116;
    //	PDFOpenOptions.height = 150;
    //}
    app.open(FileReference, PDFOpenOptions);
}

function save_document(page, type)
{
	if (type == "full")
	{
		jpgFile = new File(full_output_path + page + ".jpeg");
	}
	else
	{
        // CS3 has an adjusted resize process
        width = new UnitValue(116, "px");
        height = new UnitValue(150, "px");
        
        app.activeDocument.resizeImage(width, height, 72, ResampleMethod.BICUBIC);
        
		jpgFile = new File(thumbs_output_path + page + ".jpeg");
	}
	jpgSaveOptions = new JPEGSaveOptions();
	jpgSaveOptions.embedColorProfile = true;
	jpgSaveOptions.quality = 12;
	app.activeDocument.saveAs(jpgFile, jpgSaveOptions, true, Extension.LOWERCASE);
}

function close_document()
{
	app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);
}

for (i=1; i<=total_pages; i++)
{
	open_document(i, "thumb");
	save_document(i, "thumb");
	close_document();
}