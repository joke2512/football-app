
def noResults():
    return """
<body>
    <h1>No results for this search</h1>
    <h6>Try another please</h6>
    
</body>
"""

def showResults(data):
    html = """
<body>
<h1> Result for search:</h1>
   <table>
   <tr>
      <th>
         Name
      </th>
      <th>
         Age
      </th>
      <th>
         Nationality
      </th>
      <th>
         Club
      </th>
      <th>
         Photo
      </th>
      <th>
         Overall
      </th>
      <th>
         Value
      </th>
   </tr>
    """
    for row in data:
            html += """
            <tr>
   <td>
      {}
   </td>
   <td>
      {}
   </td>
   <td>
      {}
   </td>
   <td>
      {}
   </td>
   <td>
      <img src="{}" alt="{}">
   </td>
   <td>
      {}
   </td>
   <td>
      {}
   </td>
</tr>
            """.format(row[0], row[1], row[2], row[3], row[4], row[0], row[5], row[6])
    html += "</table></body>"
    return html

def front():
    return """
<body>
    <h1>Enter search text</h1>
    <form>
        <label>Search text:</label>
        <input id="searchQuery" type="text" value="Messi">
        <input id="submit" type="submit" value="GO" onclick="window.open(`/search?query=` + document.getElementById('searchQuery').value)">
    </form>
</body> 
    """