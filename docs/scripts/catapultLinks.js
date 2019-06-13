// List of links for Announcements tab and links table
var announcementLinks = [
    {url: "ProjectFiles/", desc: "Helpful project samples (abstract, poster template, etc.)"}
];

// List of links for Rose/catapult tab and links table
var roseLinks = [
    {url: "https://www.rose-hulman.edu/", desc: "Rose-Hulman Web Page"},
    {url: "https://www.rose-hulman.edu/csse.aspx", desc: "RHIT Computer Science &amp; Software Engineering"},
    {url: "https://moodle.rose-hulman.edu/", desc: "Rose-Hulman Moodle"},
    {
        url: "./Program/Session1/SuggestedPythonProjects.pdf",
        desc: "Python Project Descriptions (for inspiration)"
    },
    {url: "https://www.rose-hulman.edu/offices-and-services/logan-library.aspx", desc:  "Rose-Hulman Logan Library"}
];

// List of links for Python tab and links table
var pythonLinks = [
    {url:  "https://www.python.org/", desc: "Python.org Homepage"},
    {url: "https://docs.python.org/3/reference/index.html", desc: "Python Reference Manual (3.7.3)"},
    {url: "https://docs.python.org/3/tutorial/index.html", desc: "Python Tutorial (3.7.3)"},
    {url: "https://inventwithpython.com/chapters/", desc: "Python book (chapters 17-19 are a good pygame resource)"},
    {url: "https://www.tutorialspoint.com/python/", desc: "Another Good Python Tutorial"}
];

// List of links for Graphics tab and links table
var graphicsLinks = [
    {url: "https://www.pygame.org/docs/", desc: "Pygame Documentation"},
    {url: "https://github.com/fredzqm/pygameLearning", desc: "Pygame Learning templates"},
    {
        url: "https://www.pythonware.com/library/tkinter/introduction/",
        desc: "Introduction to Tkinter (module for building GUIs, probably wil not use this in Catapult)"
    }
];

// List of links for Other tab and links table
var otherLinks = [
    {url: "https://github.com/RHIT-CSSE/catapult/tree/master/Pygame%20Demos/Bubble%20Trouble", desc: "Bubble Trouble Source Files"},
    {
        url: "./SoftwareSetup/Windows_Install_Instructions.pdf",
        desc: "Install software to work on your personal Windows PC"
    },
    {
        url: "./SoftwareSetup/Mac_Install_Instructions.pdf",
        desc: "Install software to work on your Mac"
    },
	{
        url: "./SoftwareSetup/Catapult_Installation for Linux.pdf",
        desc: "Install software to work on your Linux machine"
    },
    {url: "https://www.rhventures.org/", desc: "Rose-Hulman Ventures - field trip"},
    {url: "./TakingYourProjectHome.doc", desc: "Taking Your Project Home"},
    {url: "https://goo.gl/forms/IoFjc7nQs2TvCfgP2", desc: "E-Mail Address Survey"},
    {url: "./gitlabTutorial.pdf", desc: "GitLab Instruction"}
];

// Append the list of links from announcementLinks to the provided DOM element
function displayAnnouncementsLinks(el) {
    displayLinks(announcementLinks, el);
}

// Append the list of links from roseLinks to the provided DOM element
function displayRoseLinks(el) {
    displayLinks(roseLinks, el);
}

// Append the list of links from graphicsLinks to the provided DOM element
function displayPythonLinks(el) {
    displayLinks(pythonLinks, el);
}

// Append the list of links from graphicsLinks to the provided DOM element
function displayGraphicsLinks(el) {
    displayLinks(graphicsLinks, el);
}

// Appends the list of links from otherLinks to the provided DOM element
function displayOtherLinks(el) {
    displayLinks(otherLinks, el);
}

// Append the given array of links to the given DOM element
function displayLinks(arrayOfLinks, el) {
    $.each(arrayOfLinks, function(index, value) {
        $(el).append(
            $('<li>').append(
                $('<a>').attr('href', value.url).append(value.desc)
            )
        );
    });
}
