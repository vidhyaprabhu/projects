package controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import dto.Greeting;



@RestController
@RequestMapping(value="sample")
class GreetingController {

	private static final String template = "Hello, %s!";
	 private static int counter=0;
	public GreetingController() {
		// TODO Auto-generated constructor stub
	}
	

	@RequestMapping(value="sayVidhyaName",method=RequestMethod.GET)
	 public String sayVidhyaName() {
	        return "Hey !!This is Vidhya Priyadarshini Prabhu";
	    }
	
	  @RequestMapping(value="/greeting",method=RequestMethod.GET)
	    public Greeting greeting(@RequestParam(value="name", defaultValue="World") String name) {
	        return new Greeting(counter++,
	                            String.format(template, name));
	    }
	  
	  

}
