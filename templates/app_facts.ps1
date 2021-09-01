 # Read Registry Values
 $Application = (Get-WmiObject -class win32_product)

 @{
    InstalledApp = $Application.Name
    
 }

  
