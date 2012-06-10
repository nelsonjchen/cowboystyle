# A sample Guardfile
# More info at https://github.com/guard/guard#readme

guard :shell do
    watch ('style.scss') do
        `sass style.scss:style.css`
        Kernel.sleep(1)
        `python deploy.py user.config`
    end
end 
