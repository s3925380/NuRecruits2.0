document.getElementById('buttonemerg').addEventListener('click', function()
 {
  document.querySelector('.ebutton').style.display = 'flex';
});

document.querySelector('.closebutton').addEventListener('click', function()
{
  document.querySelector('.ebutton').style.display = 'none';
});
