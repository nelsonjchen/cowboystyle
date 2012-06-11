# A sample Guardfile
# More info at https://github.com/guard/guard#readme

guard :shell do
    watch (%r{^style\.scss$}) do |m|
        `rake deploy`
        puts m[0] + " has changed."
        sleep 0
    end
end 
