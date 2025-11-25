## GPP Proposal PDF Generator

The goal is to produce a service that takes two arguments:
1. Proposal Reference
2. PDF Type:
    1. Gemini DARP
    2. Gemini Standard
    3. Gemini No Investigators
    4. Gemini Investigators at End
    5. Chile
    6. NOIRLab DARP  

and return a PDF summary of the proposal.

### Initial Investigation

The first step is to research the available options for generating a PDF summary.
Some things to consider:
- Template support
- Usability
- Performance
- Maintainability

A few options to investigate:
- [carbone](https://github.com/carboneio/carbone)
- [pdfme](https://pdfme.readthedocs.io)
- [borb](https://borbpdf.com)
- [Jinja2](https://pypi.org/project/Jinja2)
- [fpdf2](https://pypi.org/project/fpdf2)

### PDF Summary

The PDF summary should follow the PIT [examples](#pdf-examples) listed below with additions for new features enabled by GPP.

- List of groups / cadences
- List of scheduling windows if N<=5 else say "N timing windows from date1 - date2"

### PDF Examples

Example PDFs created by the PIT:
- [Chile](PIT-PDFs/PIT_Chile.pdf)
- [Gemini DARP](PIT-PDFs/PIT_Gemini_DARP.pdf)
- [Gemini Investigators at End](PIT-PDFs/PIT_Gemini_Investigators_At_End.pdf)
- [Gemini No Investigators](PIT-PDFs/PIT_Gemini_No_Investigators.pdf)
- [Gemini Standard](PIT-PDFs/PIT_Gemini_Standard.pdf)
- [NOIRLab DARP](PIT-PDFs/PIT_NOIRLab_DARP.pdf)

### Database query

The database provides a GraphQL API.
One may read the API documentation and make API queries at:
https://lucuma-postgres-odb-dev.herokuapp.com/playground.html

One may also try the supplied example query script:  [get-proposal-details.py](get-proposal-details.py)

### PDF Attachments

PIs attach 1-2 PDF files to their proposal.
These may be listed via a GraphQL query, e.g. [list-attachments.py](list-attachments.py)  
and downloaded using `requests` e.g. [download-attachments.py](download-attachments.py).

### ITC plots

We have the choice of either having the odb generate the ITC charts or we 
could query the ITC and generate the plots with matplotlib.

### gpp-client

Eventually the queries used by gpp-pdf could be included in the 
software group supported [gpp-client](https://github.com/gemini-hlsw/gpp-client).

### Partners

For reference, each partner currently uses:
* ar - da 
* br - da
* ca - da
* cl - cl
* kr - da
* uh - gs 
* us - us
* lp - da
* sip - da 
* sub - da
* gt - gs
* cfh - gs 
* sv - gsiend 
* ds - gsiend 
* ft - gsnoi 
* dt - gs 
* pw - gs
