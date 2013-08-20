    /*RFPV - Dialog code*/
    //variables globales para la acción
    var currentRecordId=-1; /* Current record Id */
    var currentURLAction=''; /* Current URL action */
    
    $(document).ready(function() {
        /*
        $('#windowTitleDialog').bind('show', function () {
            document.getElementById ("xlInput").value = document.title;
        });
        */
    }); 
    
    function newDialogShow(url) {
        $("#newDialog").modal();
        currentRecordId=-1;
        currentURLAction=url;
        // POST via ajax
        $.post(
            url,
            {dataAction:'new'},            
            function(data) {
                $('#newResult').html(data);
            }
        );
        //return false dont process href on a       
        return false;
    };
    
    function newDialogClose() {
        $('#newDialog').modal('hide'); 
    };
    
    function newDialogSave() {
        // POST form via ajax
        $.post(
            currentURLAction,
            $('form#datamanager-new').serialize(),
            function(data) {
                if (data.result==true) {
                    // Data added, reload current page
                    location.reload();
                } else {
                    alert(data.message);
                }
            },
            'json' //data returned is json            
        );
        newDialogClose();
        currentRecordId=-1;
        currentURLAction='';
    };
    
    function editDialogShow (url,recordId) {
        $("#editDialog").modal();
        currentRecordId=recordId;
        currentURLAction=url;
        // POST via ajax
        $.post(
            url,
            {dataAction:'edit', dataId:recordId},            
            function(data) {
                $('#editResult').html(data);
            }
        );        
        //return false dont process href on a
        return false;
    };
    
    function editDialogClose() {
        $('#editDialog').modal('hide'); 
    };
    
    function editDialogSave() {
        // POST form via ajax
        $.post(
            currentURLAction,
            $('form#datamanager-edit').serialize(),
            function(data) {
                if (data.result==true) {
                    // Data added, reload current page
                    location.reload();
                } else {
                    alert(data.message);
                }
            },
            'json' //data returned is json            
        );
        editDialogClose();
        currentRecordId=-1;
        currentURLAction='';
    };  

    function deleteDialogShow(url,recordId) {
        $("#deleteDialog").modal();
        currentRecordId=recordId;
        currentURLAction=url;
        //Write HTML table of record to modal dialog data area
        var title=tableGetHeaders();
        var data=tableGetRowById(currentRecordId);
        tableWrite(title, data, "deleteResult");
        //return false dont process href on a
        return false;
    };
    
    function deleteDialogClose() {
        $('#deleteDialog').modal('hide'); 
    };
    
    function deleteDialogDelete() {
        $.post(
            currentURLAction,
            {dataAction:'delete', dataId:currentRecordId},            
            function(data) {
                //Parse string as JSON
                // var jsonData = jQuery.parseJSON(data);
                if (data.result==true) {
                    // Delete row?
                    //tableDeleteRowById(currentRecordId);
                    // Reload current page
                    location.reload();
                } else {
                    alert(data.message);
                }
            },
            'json' //data returned is json            
        );        
        deleteDialogClose();
        currentRecordId=-1;
        currentURLAction='';
    };  

    function deleteAllDialogShow(url) {
        $("#deleteAllDialog").modal();
        currentRecordId=-1;
        currentURLAction=url;
        //return false dont process href on a
        return false;
    };
    
    function deleteAllDialogClose() {
        $('#deleteAllDialog').modal('hide'); 
    };
    
    function deleteAllDialogDelete() {
        $.post(
            currentURLAction,
            {dataAction:'deleteAll'},            
            function(data) {
                //Parse string as JSON
                // var jsonData = jQuery.parseJSON(data);
                if (data.result==true) {
                    // Delete row?
                    //tableDeleteRowById(currentRecordId);
                    // Reload current page
                    location.reload();
                } else {
                    alert(data.message);
                }
            },
            'json' //data returned is json            
        );        
        deleteDialogClose();
        currentRecordId=-1;
        currentURLAction='';
    };
    
    function tableWrite(tit, dat, target) {
        /** Write html table with tit, dat
        in this target
        */
        var html = '<table class="show-data">\n';
        len = dat.length;
        for (var i = 0; i < len; i++)
        {
            html += '<tr><td class="cell-title">' + tit[i] + '</td><td class="cell-data">' + dat[i] + '</td></tr>';
        }
        html += '</table>\n';
        $('#' + target).html(html);
    }
    
    function tableGetRowById(rowId, initCol, endCol) {
        /** Get row (total o partoally) by his id (<tr id=1>) and return
        an array 
        */
        cellArr = new Array();
        // Get text of each cell in this table row
        $('table tr#' + rowId + ' td').each(function(){
            cellArr.push($(this).text());
        });
        
        if (typeof(initCol)==='undefined') {
            initCol=0;
        }
        
        // Dont get last col 
        if (typeof(endCol)==='undefined') {
            if (cellArr.length==1) {
                endCol=0;
            } else {
              endCol=cellArr.length-1;  
            }
        }
        
        return cellArr.slice( initCol, endCol);
    };

    function tableGetHeaders(initCol, endCol) {
        /** Get heders (total o partoally) of a table
        */    
        cellArr = new Array();
        // Get text of each cell in this table row
        $('table tr th').each(function(){
            cellArr.push($(this).text());
        });
        
        if (typeof(initCol)==='undefined') {
            initCol=0;
        } else {
            if ( (initCol<0) || (initCol>(cellArr.length-1)) ) {
                initCol=0;
            }
        } 
        
        // Dont get last col 
        if (typeof(endCol)==='undefined') {
            endCol=cellArr.length-1;
        } else {
            if ( (endCol<0) || (endCol>(cellArr.length-1)) ) {
                endCol=initCol+1;
            }
        }
        
        return cellArr.slice(initCol, endCol);
    };
    
    function tableDeleteRowById(rowId) {
        /** Delete arow in a table by his id 
        */
        $('table tr#' + rowId).remove();
    };    
